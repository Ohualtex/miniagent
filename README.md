# Mini Agent — ~100 satırda local AI asistanı

Bir dosya. Sıfır bağımlılık. Makinende çalışan bir AI agent.

Bu repo, modern "agent" sistemlerinin (Claude Code, OpenClaw, LangChain, vb.) altında dönen mantığı **çıplak haliyle** göstermek için yazıldı. ~110 satır Python, sadece standart kütüphane.

## Neden bu repo var?

- **Local çalışır** — bulut yok, ücret yok, veri makinenden çıkmaz.
- **Sıfır `pip install`** — yalnız Python stdlib (`urllib`, `json`, `os`).
- **Tek dosya** — agent mantığının tamamı [`agent.py`](agent.py)'de, okunur.
- **Eğitim odaklı** — yorumlar Türkçe, kavramlar bu README'de açıklı.

> *"Bir agent aslında ne kadar basit?"* sorusuna **somut bir cevap**.

---

## Önce ne lazım?

- macOS (Apple Silicon önerilir) ya da Linux
- Python 3.10+
- ~5 GB boş disk (model için)
- ~8 GB RAM (16 GB daha rahat)

---

## 5 dakikada kurulum

### 1. Ollama'yı kur

Ollama, local LLM çalıştırmak için açık kaynak bir araç.

```bash
# macOS (Homebrew ile)
brew install ollama

# Diğer sistemler:
# https://ollama.com/download
```

### 2. Servisi başlat

```bash
brew services start ollama
# veya foreground:  ollama serve
```

### 3. Modeli indir (~5 GB)

```bash
ollama pull qwen2.5:7b
```

**Neden Qwen 2.5 7B?** Multilingual (Türkçe iyi), tool calling için fine-tune edilmiş, Apache 2.0 lisanslı, M-serisi Mac'te ~30-60 token/sn üretiyor.

### 4. Repo'yu klonla ve çalıştır

```bash
git clone <bu-repo-url>
cd mini-agent
python3 agent.py
```

Karşına bir prompt gelecek:

```
Mini Agent (qwen2.5:7b) — cikmak icin 'q'

Sen:
```

Çıkmak için: `q` veya `Ctrl+C`.

---

## İlk deneme

### Basit hesap

```
Sen: 37 carpi 89 kac eder?
  [tool] calculator({'expression': '37*89'})
  [out ] 3293

Agent: 37 çarpım 89, sonuc 3293'e eşittir.
```

Modelin **kendisi karar verdi** ki bu işe `calculator` lazım, argümanı kendisi hazırladı, sonucu okudu, doğal dilde cevapladı. Senin yazdığın kod sadece *"hesap yapan bir fonksiyon var"* dedi — gerisi modelin.

### Klasör listeleme

```
Sen: ~/Desktop/mini-agent/ klasorunde hangi dosyalar var?
  [tool] list_files({'directory': '~/Desktop/mini-agent/'})
  [out ] agent.py

Agent: `~/Desktop/mini-agent/` klasöründe `agent.py` adlı bir dosya var.
```

### Hata gördüğünde geri konuşması

```
Sen: ~/Documents/notlar.txt dosyasini oku
  [tool] read_file({'path': '~/Documents/notlar.txt'})
  [out ] Hata: [Errno 2] No such file or directory: ...

Agent: Belirttiğiniz dosya bulunamadı. Yolu kontrol eder misiniz?
```

Tool hata döndü → model bunu okuyup **kullanıcıya açıkladı**. Bu döngünün gücü burada: model gerçek dünya geri bildirimine adapte oluyor.

---

## Perdenin arkasında: bir agent'ın 4 parçası

```
┌─────────────────────────────────────────────────────┐
│  1. LLM (beyin)         →  Qwen 2.5 7B              │
│  2. Tools (eller)       →  Python fonksiyonları     │
│  3. Agent loop (döngü)  →  run_agent() fonksiyonu   │
│  4. Memory / context    →  messages listesi         │
└─────────────────────────────────────────────────────┘
```

Modelin tek işi **bir sonraki adımı seçmek**. Eylem senin kodun. Loop'u kuran da senin kodun. Model **stateless** — her çağrıda geçmişi sen yolluyorsun.

## Agent döngüsü nasıl çalışıyor?

```
   kullanıcı sorusu
        │
        ▼
   ┌───────────────────────────────┐
   │ messages = [system, user]     │
   └─────────────┬─────────────────┘
                 │
                 ▼
   ┌───────────────────────────────┐
   │ Ollama'ya istek (POST /chat)  │◄────┐
   └─────────────┬─────────────────┘     │
                 │                       │
                 ▼                       │
   ┌───────────────────────────────┐     │
   │ model cevabı geldi            │     │
   │ messages.append(cevap)        │     │
   └─────────────┬─────────────────┘     │
                 │                       │
            tool çağrısı?                │
            ┌────┴────┐                  │
          evet        hayır              │
            │           │                │
            ▼           ▼                │
   ┌────────────┐  ┌─────────────────┐   │
   │ tool çalış │  │ cevabı kullanı- │   │
   │ sonucu mes-│  │ cıya göster &   │   │
   │ sages'a ekle│ │ bitir           │   │
   └─────┬──────┘  └─────────────────┘   │
         │                               │
         └──────── döngüye dön ──────────┘
```

`agent.py` içinde tam olarak bu var, ~20 satır:

```python
def run_agent(user_input, max_iter=6):
    messages = [
        {"role": "system", "content": "Sen yardimci bir asistansin..."},
        {"role": "user", "content": user_input},
    ]
    for _ in range(max_iter):
        msg = chat(messages)              # Ollama'ya gönder
        messages.append(msg)

        tool_calls = msg.get("tool_calls") or []
        if not tool_calls:
            print(f"\nAgent: {msg['content']}")
            return

        for call in tool_calls:
            name = call["function"]["name"]
            args = call["function"]["arguments"]
            result = TOOLS_MAP[name](**args)        # tool'u çalıştır
            messages.append({"role": "tool", "content": str(result)})
```

Bu kadar. Claude Code, LangChain, OpenClaw — hepsinin altında bu döngünün varyantları var.

---

## Yeni tool ekleme — 3 adım

Diyelim ki **hava durumu** yeteneği eklemek istiyorsun.

### Adım 1: Python fonksiyonu yaz

```python
def get_weather(city: str) -> str:
    """Wttr.in'den hava bilgisi çek (API key gerekmez)."""
    url = f"https://wttr.in/{city}?format=3"
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8"})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            return r.read().decode().strip()
    except Exception as e:
        return f"Hata: {e}"
```

### Adım 2: `TOOLS_MAP`'e kayıt

```python
TOOLS_MAP["get_weather"] = get_weather
```

### Adım 3: JSON şemayı tanımla

```python
TOOLS_SCHEMA.append({
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Bir şehrin güncel hava durumunu döner.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Şehir adı, örn: 'Istanbul', 'Ankara'"
                }
            },
            "required": ["city"]
        }
    }
})
```

Bitti. Bir sonraki turda:

```
Sen: Ankara'da hava nasil?
  [tool] get_weather({'city': 'Ankara'})
  [out ] Ankara: 🌦  +12°C
Agent: Ankara'da şu an hafif yağmurlu, sıcaklık 12 derece.
```

**Üç yer, ~30 satır.** Yeteneğin kullanılır hale gelmesi için tek gereken bu.

---

## Deneyebileceğin promptlar

| Prompt | Hangi tool tetiklenir |
|---|---|
| *"127 × 43 + 9 kaç eder?"* | `calculator` |
| *"Masaüstümde neler var?"* | `list_files` |
| *"~/Desktop/notes.txt dosyasını oku"* | `read_file` |
| *"İstanbul'un nüfusu kaç?"* | tool yok → modelin kendi bilgisinden |
| *"Documents'ı listele, txt varsa içeriğini de göster"* | iki tool peş peşe (multi-step) |
| *"Bana bir Python fibonacci fonksiyonu yaz"* | tool yok → model kod döner (metin olarak) |

---

## Mevcut 3 tool

| Tool | İş |
|---|---|
| `list_files(directory)` | Klasördeki dosya/alt klasörleri listeler |
| `read_file(path)` | Dosya içeriğini okur (ilk 2000 karakter) |
| `calculator(expression)` | Matematik ifadesini hesaplar (`+ - * / ( )`) |

Hepsi `agent.py` içinde, ~20 satırda. İlham için bak, kendi tool'unu yaz.

---

## Sınırlar (dürüstçe)

- **Frontier model değil.** Qwen 2.5 7B, GPT-4 / Claude 4.7 seviyesinde değildir. Karmaşık çoklu adım planlama (örn. *"5 PDF'i karşılaştır, ortak temaları çıkar, sunum hazırla"*) zayıf.
- **Hallucination riski var.** Bilmediği bir konuda uydurabilir. Atıf veren tool eklemeden *"bu makale gerçek mi?"* sorma.
- **`calculator` `eval()` kullanıyor** — sadece sayı/operatör karakterleri kabul ediyor ama yeni tool eklerken `subprocess`, `eval` gibi yapılarda **çok dikkatli ol**. Production için sandbox şart.
- **Context limit.** Çok uzun tool çıktıları (50 KB+) modelin dikkatini dağıtır. `read_file` 2000 karakter limiti bunun için var.
- **Tek thread.** Çok sayıda eşzamanlı kullanıcı için tasarlanmadı. Bir kişinin terminalinde çalıştırılan bir araç.

---

## Bundan sonra büyütülebilir yönler

Bu repo bir **iskelet**. Şu yönlere genişletilebilir:

- **Daha fazla tool**: web arama, e-mail, shell, `.docx`/`.pdf` okuma
- **Skill loader** ([OpenClaw](https://github.com/openclaw/openclaw) tarzı): her yetenek ayrı bir Markdown dosyası, kataloğa göre lazy-load
- **Provider abstraction**: Ollama yerine Anthropic/OpenAI'a tek satırla geçiş
- **Web UI**: [Streamlit](https://streamlit.io) ile ~30 satırlık chat arayüzü
- **Memory**: konuşma geçmişini diske kaydet
- **RAG**: PDF/Word'leri embed et, "soru sor, kaynaktan cevap al"
- **Model swap**: `MODEL = "qwen2.5:14b"` → daha akıllı, biraz yavaş

---

## Daha fazla okuma

- [Ollama belgeleri](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Qwen 2.5 makalesi](https://arxiv.org/abs/2412.15115)
- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [ReAct: Reasoning + Acting in LLMs](https://arxiv.org/abs/2210.03629)
- [OpenClaw](https://github.com/openclaw/openclaw) — production-grade local agent gateway

---

## Lisans

MIT — özgürce kullan, fork'la, dersinde paylaş. Detay: [LICENSE](LICENSE).

---

## Notlar

Bu repo, **agent mantığını anlatan bir blog yazısının kod ekidir**. Detaylı anlatım için: *[blog yazısı linki buraya gelecek]*.

Soru/öneri için Issues bölümünü kullanabilirsiniz.
