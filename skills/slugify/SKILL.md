---
name: slugify
version: 0.1.0
description: Bir metni URL-uyumlu slug haline getirir (küçük harf, tire ayraçlı, özel karakter yok).
icon: "🔗"
example_prompt: "'Merhaba Dünya!' başlığını slug yap"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [python3]
  internet: false
tags: [slug, text, url, dev]
---

# Slugify Skill

Bir başlığı veya metni URL-uyumlu **slug**'a (küçük harf, tire ayraçlı,
sadece harf/rakam) çevirmek için Python'un `re` ve `unicodedata` modülleri
kullanılır. Türkçe karakterler ASCII'ye normalize edilir.

## Çalıştırılacak komut

**Kısa metin için:**

```
python3 -c 'import sys,re,unicodedata; t=unicodedata.normalize("NFKD",sys.argv[1]).encode("ascii","ignore").decode().lower(); print(re.sub(r"[^a-z0-9]+","-",t).strip("-"))' '<metin>'
```

`<metin>` yerine kullanıcının verdiği metni koy.

**Uzun veya özel karakter içeren metin için** (shell quoting sorunlarını
önlemek için kullanıcıdan metni geçici bir dosyaya kaydetmesini iste,
örn. `~/in.txt`):

```
python3 -c 'import sys,re,unicodedata; t=open(sys.argv[1]).read().strip(); t=unicodedata.normalize("NFKD",t).encode("ascii","ignore").decode().lower(); print(re.sub(r"[^a-z0-9]+","-",t).strip("-"))' ~/in.txt
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar — tek satırlık slug.
Türkçe karakterler ASCII'ye normalize edilir (ç→c, ş→s, ğ→g, ü→u, ö→o, ı→i).

## Hata durumları

- **`python3` bulunamadı:** Python 3 kurulması gerek.
- **Boş çıktı:** Verilen metin sadece özel karakter veya boşluksa slug boş
  kalır.
