---
name: hash-file
version: 0.1.0
description: Bir dosyanın sha256 veya md5 checksum'unu hesaplar; bütünlük doğrulaması için.
icon: "🔒"
example_prompt: "~/Downloads/installer.dmg'in sha256 hash'i ne?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [shasum]
  internet: false
tags: [hash, checksum, security, file]
---

# Hash File Skill

Bir dosyanın checksum'unu hesaplayarak bütünlüğünü doğrulamak için kullanılır.
Varsayılan algoritma sha256.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
shasum -a 256 <dosya_yolu>
```

`<dosya_yolu>` yerine kullanıcının belirttiği yolu koy. `~` desteklenir.

Kullanıcı **md5** isterse:

```
md5 <dosya_yolu>
```

`md5` macOS'ta yerleşiktir; Linux'ta `md5sum <dosya_yolu>` kullan.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- **Hash değerini** belirgin biçimde göster.
- Eğer kullanıcı karşılaştırma için bir beklenen hash verdiyse, hesaplanan ile
  eşleşip eşleşmediğini açıkça söyle.

## Hata durumları

- **Dosya bulunamadı:** Yolun doğru olup olmadığını teyit etmesini iste.
- **İzin reddedildi:** Dosyaya okuma izninin olmadığını bildir.
- **`shasum` bulunamadı:** Linux'ta `sha256sum`, macOS'ta `shasum` kurulu
  değilse uygun paketi (`coreutils`) kurmasını öner.
