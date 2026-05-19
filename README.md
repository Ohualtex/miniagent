# Mini Agent — Local AI asistanı + Skill Loader (v2)

Tek dosya. Sıfır pip bağımlılığı. Makinende çalışan bir AI agent.
Yetenekler **Markdown dosyaları** olarak yaşıyor; model bunları gerektiğinde
**lazy-load** ediyor — Anthropic Agent Skills ve [OpenClaw](https://github.com/openclaw/openclaw) gibi.

> 📚 **Hangi sürümü inceliyorsunuz?**
> Bu repo iki sürüm barındırıyor — blog yazılarına eşlik etmek için:
> - **v1**: temel agent loop, 3 hardcoded tool ([branch `v1`](https://github.com/yildirimozal/miniagent/tree/v1) · tag [`v1.0`](https://github.com/yildirimozal/miniagent/releases/tag/v1.0))
> - **v2** (bu sayfa): skill loader + lazy load ([branch `v2`](https://github.com/yildirimozal/miniagent/tree/v2) · tag [`v2.0`](https://github.com/yildirimozal/miniagent/releases/tag/v2.0))
>
> Sadece v1 ile başlamak istiyorsanız:
> `git clone --branch v1 https://github.com/yildirimozal/miniagent`

## Neden bu repo var?

- **Local çalışır** — bulut yok, ücret yok, veri makinenden çıkmaz.
- **Sıfır `pip install`** — yalnız Python stdlib (`urllib`, `json`, `subprocess`).
- **Tek dosya çekirdek** + `skills/` klasörü — okunur, fork'lanır, genişletilir.
- **Eğitim odaklı** — production değil ders kodu; her satır anlaşılabilir.

> *"Bir agent skill sistemi aslında ne kadar basit?"* sorusuna **somut bir cevap**.

---

## Mimari özeti

```
┌──────────────────────────────────────────────────────────┐
│  PRIMITIVES (her zaman var, kod olarak duruyor)          │
│    • read_file   → dosya oku                             │
│    • list_files  → klasör listele                        │
│    • bash        → shell komutu çalıştır                 │
└──────────────────────────────────────────────────────────┘
                          ▲
                          │ skill'ler bu primitive'leri çağırır
                          │
┌──────────────────────────────────────────────────────────┐
│  SKILLS (lazy-load, markdown olarak yaşıyor)             │
│    skills/                                               │
│      weather/SKILL.md            — curl ile hava durumu  │
│      find-large-files/SKILL.md   — du ile büyük dosyalar │
│      mac-notification/SKILL.md   — osascript ile bildirim│
└──────────────────────────────────────────────────────────┘
                          ▲
                          │ katalog (name + description + location)
                          │ sistem prompt'a ekleniyor
                          ▼
                   ┌──────────────┐
                   │   QWEN 2.5   │
                   │   karar verir│
                   └──────────────┘
```

**Skill = yetenek değil, talimat seti.** Asıl iş `bash` ile çalışan binary'lerde
(curl, du, osascript, ...). Skill modele *"şu komutu, şu argümanla, şöyle yorumla"*
diyor — model okuyup uyguluyor.

---

## Önce ne lazım?

- macOS (Apple Silicon önerilir) veya Linux
- Python 3.10+
- ~5 GB boş disk
- ~8 GB RAM (16 GB daha rahat)

---

## 5 dakikada kurulum

### 1. Ollama'yı kur

```bash
brew install ollama          # macOS
brew services start ollama
```

Diğer sistemler: [ollama.com/download](https://ollama.com/download).

### 2. Modeli indir (~4.7 GB)

```bash
ollama pull qwen2.5:7b
```

**Neden Qwen 2.5 7B?** Multilingual (Türkçe iyi), tool calling için
fine-tune edilmiş, Apache 2.0 lisanslı, M-serisi Mac'te 30-60 token/sn.

### 3. Repo'yu klonla ve çalıştır

```bash
git clone https://github.com/yildirimozal/miniagent
cd miniagent
python3 agent.py
```

```
Mini Agent v2 (qwen2.5:7b)
Yuklenen skill sayisi: 3
  - find-large-files: Bir klasördeki en büyük dosyaları/alt klasörleri bulur.
  - mac-notification: macOS'ta masaüstü bildirimi gösterir. Sadece Mac'te çalışır.
  - weather: Bir şehrin güncel hava durumunu söyler. İnternet bağlantısı ve curl gerekir.
Cikmak icin 'q'

Sen:
```

---

## Canlı demo

### Hava durumu — lazy-load akışı

```
Sen: Ankara'da hava nasil?
  [tool] read_file({'path': '~/Desktop/miniagent/skills/weather/SKILL.md'})
  [out ] --- name: weather description: Bir şehrin güncel hava durumunu söyler ...
  [bash] $ curl -s 'https://wttr.in/Ankara?format=3'
  [out ] ankara: 🌤️  +8°C

Agent: Ankara'da hava sıcaklığı +8°C ve güneşli bir gün geçiriyorsunuz.
```

Bakın **iki tool çağrısı arka arkaya**:
1. Önce `read_file` — skill'in talimat metnini context'e çekti
2. Sonra `bash` — talimattan çıkardığı komutu çalıştırdı
3. Sonuçtan doğal Türkçe cevabı oluşturdu

Bu **lazy-load**. Skill body'leri sistem prompt'a hiç girmedi; model sadece
kataloğu gördü, ihtiyacı olanı kendi çekti.

### Büyük dosya bulma

```
Sen: ~/Downloads klasorumdeki en buyuk dosyalari bul
  [tool] read_file({'path': '~/Desktop/miniagent/skills/find-large-files/SKILL.md'})
  [out ] ...
  [bash] $ du -ah ~/Downloads 2>/dev/null | sort -hr | head -10
  [out ] 3.0G  /Users/ozal/Downloads ...

Agent: İndirme klasörünüzdeki en büyük dosyaları buldum:
1. 3.0G  /Users/ozal/Downloads
2. 430M  /Users/ozal/Downloads/proje-arsivi
3. 404M  /Users/ozal/Downloads/A3.1 (120 Puan)
4. 388M  /Users/ozal/Downloads/proje-arsivi.rar
```

---

## Bir agent'ın 4 parçası (refresher)

```
┌─────────────────────────────────────────────────────┐
│  1. LLM (beyin)         →  Qwen 2.5 7B              │
│  2. Tools (eller)       →  3 primitive + N skill    │
│  3. Agent loop          →  run_agent() ~20 satır    │
│  4. Memory / context    →  messages listesi         │
└─────────────────────────────────────────────────────┘
```

Modelin tek işi **bir sonraki adımı seçmek**. Eylem senin kodun. Model
stateless — her çağrıda geçmişi sen yolluyorsun.

## Agent döngüsü

```
   kullanıcı sorusu
        │
        ▼
   ┌───────────────────────────────┐
   │ messages = [system+katalog,   │
   │             user]             │
   └─────────────┬─────────────────┘
                 │
                 ▼
   ┌───────────────────────────────┐
   │ Ollama'ya gönder (primitives) │◄────┐
   └─────────────┬─────────────────┘     │
                 │                       │
                 ▼                       │
            tool çağrısı?                │
            ┌────┴────┐                  │
          evet        hayır              │
            │           │                │
            ▼           ▼                │
   ┌────────────┐  ┌─────────────────┐   │
   │ tool çalış │  │ cevabı kullanı- │   │
   │ sonucu mes-│  │ cıya göster &   │   │
   │ sages'a ekle│  │ bitir           │   │
   └─────┬──────┘  └─────────────────┘   │
         │                               │
         └──────── döngüye dön ──────────┘
```

`agent.py:run_agent()` içinde, ~25 satır.

---

## Skill formatı

Her skill bir **klasör** + içinde tek bir **`SKILL.md`**:

```
skills/
  weather/
    SKILL.md
  find-large-files/
    SKILL.md
  mac-notification/
    SKILL.md
```

`SKILL.md`'nin yapısı:

```markdown
---
name: weather
description: Bir şehrin güncel hava durumunu söyler.
---

# Weather Skill

Bir şehrin güncel hava durumunu öğrenmek için wttr.in servisini kullan.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

    curl -s 'https://wttr.in/<şehir>?format=3'

## Sonuç geldikten sonra

Çıktıyı kullanıcıya doğal Türkçe ile aktar.
```

İki kritik alan:
- **`name`** + **`description`** — modele **katalog kartı** olarak gider
- **Body** — model bu skill'i seçince **detaylı talimat** olarak okur

---

## Lazy loading — neden önemli?

100 skill'iniz olsa, her birinin ~50 satırlık body'sini her prompt'a koysanız
modelin context'i şişer. Lazy loading şu mantıkla çözüyor:

1. **Başlangıç**: sistem prompt'a sadece **katalog** giriyor (~5 satır/skill)
2. **Kullanıcı bir şey sorar** → model uygun skill'i kataloğdan seçer
3. **`read_file(<skill location>)`** ile body'i çeker (sadece o)
4. Talimatı uygular

OpenClaw bu pattern'i 100+ skill ile ölçeklendiriyor. Bizimki minimal hâli.

---

## Yeni skill ekleme — sıfır Python

Hava durumu için zaten bir skill var. Diyelim ki bir **GitHub issue listeleyici**
istiyorsunuz. Sadece bir dosya yazıyorsunuz:

```bash
mkdir skills/gh-issues
```

`skills/gh-issues/SKILL.md`:

```markdown
---
name: gh-issues
description: Bir GitHub repo'sundaki açık issue'ları listeler. gh CLI gerekli.
---

# GitHub Issues Skill

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

    gh issue list --repo <owner/repo> --limit 10

## Sonuç geldikten sonra

Issue başlıklarını numaralandırılmış liste halinde kullanıcıya göster.
```

Agent'ı yeniden başlatın. Katalogda yeni skill'i göreceksiniz. Test:

```
Sen: openclaw repo'sunda son issue'lar neler?
  [tool] read_file({'path': '~/.../skills/gh-issues/SKILL.md'})
  [out] ...
  [bash] $ gh issue list --repo openclaw/openclaw --limit 10
  ...
```

**Tek Python satırı yazmadan yeni yetenek.** OpenClaw'ın temel sloganı.

---

## Sınırlar — dürüstçe

Bu reponun amacı eğitim. Production değil. Bilmeniz gerekenler:

**Tool kullanım tutarlılığı.** Qwen 2.5 7B multi-step tool kullanımında
**zaman zaman tutarsız**. Aynı sorgu bazen skill'i okuyor, bazen direkt bash
ile gidiyor, bazen "skill yok" diyor. Üç başlık altında çözüm:

1. **SKILL.md'yi imperative yazın** — "şunu yap" gibi direkt ifadeler. Örnek
   çıktı göstermek tehlikeli (model halüsine eder).
2. **Kod-seviyesinde müdahale** ekleyin — bu repo'da `agent.py` SKILL.md
   okumasından sonra modele sentetik bir hatırlatma enjekte ediyor.
3. **Daha büyük model**: `qwen2.5:14b` (~9 GB) tool use'da belirgin daha
   güvenilir. `MODEL = "qwen2.5:14b"` ile geçilir.

**`bash` tehlikeli.** LLM rastgele komut üretebilir. Bu kod subprocess
+ 30 saniye timeout ile sınırlandı, ama **production için sandbox şart**
(Docker, Firecracker, gVisor, vs.).

**Halüsinasyon riski.** 7B modeller bilmedikleri yerde uydurur. Atıf doğrulayan
tool eklemeden *"bu makale gerçek mi?"* sormayın.

**Context limit.** Tool çıktıları MAX_OUTPUT=4000 karaktere kesiliyor.
Çok büyük dosya/komut çıktıları için chunking gerekir.

---

## Bundan sonra ne yapılabilir?

Bu repo bir **iskelet**. OpenClaw'a doğru büyütmek için sıradaki adımlar:

- **Provider abstraction**: Ollama yerine Anthropic/OpenAI'a tek satırla geçiş
- **Daha çok skill**: web arama, e-mail, takvim, .docx okuma, vs.
- **Skill katmanları**: workspace skills > user skills > bundled skills hierarchy
- **MCP integrasyonu**: standart protokolle dış sistemlere bağlan
- **Memory katmanı**: konuşma geçmişi, RAG, vector DB
- **Web UI**: Streamlit ile chat arayüzü
- **Onay sistemi**: tehlikeli bash komutları için kullanıcı onayı

---

## Daha fazla okuma

- [Ollama API](https://github.com/ollama/ollama/blob/main/docs/api.md)
- [Qwen 2.5 makalesi](https://arxiv.org/abs/2412.15115)
- [Anthropic — Building effective agents](https://www.anthropic.com/research/building-effective-agents)
- [Anthropic — Agent Skills](https://www.anthropic.com/news/skills) — bu reponun ilham kaynağı
- [OpenClaw](https://github.com/openclaw/openclaw) — production-grade local agent gateway
- [ReAct paper](https://arxiv.org/abs/2210.03629)

---

## Versiyonlar

| Sürüm | Ne içerir | Direkt göz at | Klonla |
|---|---|---|---|
| **v1** | Temel agent loop, 3 hardcoded tool (`list_files`/`read_file`/`calculator`), ~117 satır | [tree/v1](https://github.com/yildirimozal/miniagent/tree/v1) | `git clone --branch v1 https://github.com/yildirimozal/miniagent` |
| **v2** | Skill loader + lazy load (OpenClaw stili), 3 primitive + 3 skill, ~257 satır | [tree/v2](https://github.com/yildirimozal/miniagent/tree/v2) | `git clone --branch v2 https://github.com/yildirimozal/miniagent` |
| **main** | v2 ile aynı (geliştirme branch'i) | [tree/main](https://github.com/yildirimozal/miniagent) | `git clone https://github.com/yildirimozal/miniagent` |

Tag'ler: [`v1.0`](https://github.com/yildirimozal/miniagent/releases/tag/v1.0) · [`v2.0`](https://github.com/yildirimozal/miniagent/releases/tag/v2.0)

Eski versiyona git'siz erişim: GitHub'da [tree/v1](https://github.com/yildirimozal/miniagent/tree/v1) sayfasını açıp yeşil **"Code"** butonu → **"Download ZIP"**.

---

## Lisans

MIT — özgürce kullan, fork'la, dersinde paylaş. Detay: [LICENSE](LICENSE).

---

## Notlar

Bu repo, agent mimarisini anlatan **iki blog yazısının** kod ekidir:

1. *"100 Satır Python ile Kendi Yerel AI Asistanınızı Yazın"* — v1, temel agent loop
2. *"OpenClaw Mimarisi Mini Sürümde: Skill Loader ve Lazy Load"* — v2, bu yazı

Soru/öneri için Issues bölümünü kullanabilirsiniz.
