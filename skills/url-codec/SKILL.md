---
name: url-codec
version: 0.1.0
description: Metni URL-encode veya URL-decode eder (percent encoding).
icon: "🔣"
example_prompt: "Şu metni URL encode et: hello world & friends"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [python3]
  internet: false
tags: [url, encode, decode, dev]
---

# URL Codec Skill

Metni URL-uyumlu (percent-encoded) hâle getirmek veya geri çevirmek için
Python'un `urllib.parse` modülü kullanılır.

## Çalıştırılacak komut

**Encode (kısa metin):**

```
python3 -c 'import sys,urllib.parse; print(urllib.parse.quote(sys.argv[1]))' '<metin>'
```

**Decode (kısa metin):**

```
python3 -c 'import sys,urllib.parse; print(urllib.parse.unquote(sys.argv[1]))' '<metin>'
```

**Uzun veya özel karakter içeren metin için** (shell quoting sorunlarını
önlemek için kullanıcıdan metni geçici bir dosyaya kaydetmesini iste):

Encode:

```
python3 -c 'import sys,urllib.parse; print(urllib.parse.quote(open(sys.argv[1]).read().rstrip("\n")))' ~/in.txt
```

Decode:

```
python3 -c 'import sys,urllib.parse; print(urllib.parse.unquote(open(sys.argv[1]).read().rstrip("\n")))' ~/in.txt
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Encode sonucu: `hello%20world%20%26%20friends` gibi percent-encoded metin
- Decode sonucu: orijinal okunabilir metin

## Hata durumları

- **`python3` bulunamadı:** Python 3 kurulması gerek.
- **Dosya bulunamadı:** Yolu teyit et.
