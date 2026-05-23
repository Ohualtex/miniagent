"""
Mini Agent v2 — Lazy-load Skill Loader
OpenClaw mimarisinden ilham: skill = markdown talimat seti,
primitives = kod olarak duran az sayida temel arac.

Calistir:  python3 agent.py
Cik:       q  (veya Ctrl+C)
"""
import json
import os
import subprocess
import urllib.error
import urllib.request
from pathlib import Path

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:7b"
SKILLS_DIR = Path(__file__).parent / "skills"
BASH_TIMEOUT = 30      # saniye
MAX_OUTPUT = 4000      # tool ciktisi icin karakter limiti


# =========================================================
# 1) PRIMITIVES — Her zaman yuklenen temel araclar
#    Bunlar Python kodu. Skill'ler bunlari "kullanarak" calisir.
# =========================================================
def read_file(path: str) -> str:
    try:
        text = Path(os.path.expanduser(path)).read_text(encoding="utf-8")
        return text[:MAX_OUTPUT]
    except Exception as e:
        return f"Hata: {e}"


def list_files(directory: str) -> str:
    try:
        items = os.listdir(os.path.expanduser(directory))
        return "\n".join(sorted(items)) if items else "(bos klasor)"
    except Exception as e:
        return f"Hata: {e}"


def bash(command: str) -> str:
    """Shell komutu calistir. UYARI: production icin sandbox + onay sart."""
    print(f"  [bash] $ {command}")
    try:
        r = subprocess.run(
            command, shell=True, capture_output=True, text=True,
            timeout=BASH_TIMEOUT,
        )
        out = (r.stdout + r.stderr).strip()
        if not out:
            out = f"(exit {r.returncode}, no output)"
        return out[:MAX_OUTPUT]
    except subprocess.TimeoutExpired:
        return f"Hata: {BASH_TIMEOUT} saniye icinde tamamlanmadi."
    except Exception as e:
        return f"Hata: {e}"


PRIMITIVES = {"read_file": read_file, "list_files": list_files, "bash": bash}

PRIMITIVES_SCHEMA = [
    {"type": "function", "function": {
        "name": "read_file",
        "description": "Bir dosyanin icerigini okur. Skill kullanmadan once SKILL.md okumak icin gerekli.",
        "parameters": {"type": "object", "required": ["path"],
            "properties": {"path": {"type": "string", "description": "Dosya yolu (~ destekli)"}}}}},
    {"type": "function", "function": {
        "name": "list_files",
        "description": "Bir klasordeki dosya ve alt klasorleri listeler.",
        "parameters": {"type": "object", "required": ["directory"],
            "properties": {"directory": {"type": "string"}}}}},
    {"type": "function", "function": {
        "name": "bash",
        "description": "Shell komutu calistirir. Skill'ler genellikle bash komutlari icerir.",
        "parameters": {"type": "object", "required": ["command"],
            "properties": {"command": {"type": "string", "description": "Calistirilacak shell komutu"}}}}},
]


# =========================================================
# 2) SKILL LOADER — Markdown dosyalarini katalog halinde yukle
# =========================================================
def parse_frontmatter(text: str) -> dict:
    """Basit YAML-vari frontmatter parser. Sadece duz 'k: v' satirlari destekli."""
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    result = {}
    for line in text[3:end].strip().splitlines():
        if ":" not in line or line.lstrip().startswith("#"):
            continue
        k, _, v = line.partition(":")
        v = v.strip().strip('"').strip("'")
        result[k.strip()] = v
    return result


def load_skill_catalog(skills_dir: Path) -> list[dict]:
    """skills/ altinda her alt klasorde SKILL.md ara, katalogu olustur."""
    catalog = []
    if not skills_dir.exists():
        return catalog
    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        skill_md = skill_dir / "SKILL.md"
        if not skill_md.exists():
            continue
        try:
            text = skill_md.read_text(encoding="utf-8")
        except Exception:
            continue
        fm = parse_frontmatter(text)
        name = fm.get("name", "").strip()
        desc = fm.get("description", "").strip()
        if not name or not desc:
            continue
        catalog.append({
            "name": name,
            "description": desc,
            "location": str(skill_md.resolve()),
        })
    return catalog


def format_skill_catalog(catalog: list[dict]) -> str:
    """OpenClaw stili XML katalog (sistem prompt'a eklenir)."""
    if not catalog:
        return ""
    lines = [
        "",
        "Asagida kullanabilecegin skill'ler var. Kullanicinin istegi bir skill'in",
        "description'i ile eslesiyor ise, o skill'i kullan: once `location` yolunu",
        "`read_file` ile oku, sonra icindeki komutu `bash` ile calistir.",
        "",
        "<available_skills>",
    ]
    for s in catalog:
        lines += [
            "  <skill>",
            f"    <name>{s['name']}</name>",
            f"    <description>{s['description']}</description>",
            f"    <location>{s['location']}</location>",
            "  </skill>",
        ]
    lines.append("</available_skills>")
    return "\n".join(lines)


# =========================================================
# 3) OLLAMA istek
# =========================================================
def chat(messages):
    payload = json.dumps({
        "model": MODEL, "messages": messages,
        "tools": PRIMITIVES_SCHEMA, "stream": False,
        "options": {"temperature": 0.2},  # dusuk ama tam sifir degil (sifirda 7B takilabiliyor)
    }).encode()
    req = urllib.request.Request(OLLAMA_URL, data=payload,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())["message"]
    except urllib.error.URLError as e:
        raise RuntimeError(
            f"Ollama'ya baglanilamadi ({OLLAMA_URL}). "
            f"Calisiyor mu? 'brew services start ollama' veya 'ollama serve'. "
            f"Detay: {e.reason}"
        )


# =========================================================
# 4) AGENT LOOP
# =========================================================
SYSTEM_PROMPT = """Sen yardimci bir Turkce asistansin.

Elinde uc temel arac var: read_file, list_files, bash.

Bunlara ek olarak yuklenebilecek "skill"ler var. Skill = belirli bir gorev
icin hazirlanmis Markdown talimat seti. Bir kullanici istegi icin uygun bir
skill varsa su sirayi izle:
  1. Katalogdan dogru skill'i sec.
  2. `read_file(<skill location>)` ile dosyasini oku.
  3. SKILL.md'deki komutu `bash` tool'u ile CALISTIR
     (komutu metin olarak gosterip durma; tool'u kullanip sonuc al).
  4. Tool sonucunu aldiktan sonra kullaniciya dogal Turkce ile sun.

Eger katalogda uygun bir skill YOKSA, dogrudan kendi bilginle ya da bash ile
cevapla.
"""


def run_agent(user_input: str, catalog: list[dict], max_iter: int = 8):
    system_with_catalog = SYSTEM_PROMPT + format_skill_catalog(catalog)
    messages = [
        {"role": "system", "content": system_with_catalog},
        {"role": "user", "content": user_input},
    ]
    for _ in range(max_iter):
        msg = chat(messages)
        messages.append(msg)

        tool_calls = msg.get("tool_calls") or []
        if not tool_calls:
            content = (msg.get("content") or "").strip()
            if content:
                print(f"\nAgent: {content}\n")
            return

        skill_md_read = False
        for call in tool_calls:
            name = call["function"]["name"]
            args = call["function"]["arguments"]
            if name not in PRIMITIVES:
                result = f"Hata: '{name}' bilinmeyen tool."
            else:
                if name != "bash":
                    print(f"  [tool] {name}({args})")
                try:
                    result = PRIMITIVES[name](**args)
                except TypeError as e:
                    # Model bozuk arguman uretirse oturum dusmesin
                    result = f"Hata: tool '{name}' icin gecersiz arguman — {e}"
                except Exception as e:
                    result = f"Hata: tool '{name}' calistirilamadi — {e}"
                preview = str(result)[:120].replace("\n", " ")
                print(f"  [out ] {preview}{'...' if len(str(result)) > 120 else ''}")
            messages.append({"role": "tool", "content": str(result)})

            # SKILL.md okumasini isaretle; enjeksiyon tum tool sonuclari
            # eklendikten sonra, dongu disinda yapilir (cogul tool_calls
            # senaryosunda tool/user/tool sirasini bozmamak icin).
            if (name == "read_file" and isinstance(args, dict)
                    and "SKILL.md" in str(args.get("path", ""))):
                skill_md_read = True

        # === Deterministik mudahale ===
        # Model bir SKILL.md okuduysa, bir sonraki turda komutu
        # CALISTIRMAYI unutmasın diye sentetik bir hatırlatma ekle.
        if skill_md_read:
            messages.append({
                "role": "user",
                "content": (
                    "[SISTEM] SKILL.md icerigini aldın. SIMDI uygun komutu "
                    "`bash` tool'u ile CALISTIR. SKILL.md'deki ornek ciktilari "
                    "cevap olarak KULLANMA — gercek komutu calistir ve gercek "
                    "sonucu kullan. Komutu yalniz aciklama, calistir."
                )
            })

    print("\n(Max iteration asildi.)\n")


# =========================================================
# 5) MAIN
# =========================================================
if __name__ == "__main__":
    catalog = load_skill_catalog(SKILLS_DIR)
    print(f"Mini Agent v2 ({MODEL})")
    print(f"Yuklenen skill sayisi: {len(catalog)}")
    for s in catalog:
        print(f"  - {s['name']}: {s['description']}")
    if not catalog:
        print("  (skills/ klasoru bos veya yok)")
    print("Cikmak icin 'q'\n")

    while True:
        try:
            q = input("Sen: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in ("q", "quit", "exit"):
            break
        if q:
            try:
                run_agent(q, catalog)
            except RuntimeError as e:
                print(f"\nHata: {e}\n")
