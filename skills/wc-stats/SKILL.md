---
name: wc-stats
version: 0.1.0
description: Bir dosyanın satır, kelime ve karakter sayısını verir.
icon: "📏"
example_prompt: "~/notes.md kaç satır?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [wc]
  internet: false
tags: [text, count, file]
---

# WC Stats Skill

Bir dosyanın metinsel istatistiklerini (satır/kelime/karakter sayısı) çıkarmak
için `wc` kullanılır. Hem macOS hem Linux'ta yerleşiktir.

## Çalıştırılacak komut

**Hepsi birden (satır, kelime, karakter, byte):**

```
wc <dosya_yolu>
```

**Sadece satır sayısı:**

```
wc -l <dosya_yolu>
```

**Sadece kelime sayısı:**

```
wc -w <dosya_yolu>
```

**Sadece karakter sayısı:**

```
wc -m <dosya_yolu>
```

`<dosya_yolu>` yerine kullanıcının belirttiği yolu koy. `~` desteklenir.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Hangi sayıyı sorduysa onu öne çıkar (ör. "dosya 142 satır")
- Hepsi sorulmuşsa: satır, kelime, karakter ve byte sayılarını liste hâlinde
  göster
- `wc -m` ile karakter, `wc -c` ile byte sayısı verir; UTF-8 dosyalarda
  bu ikisi farklıdır — kullanıcıya bunu hatırlat

## Hata durumları

- **Dosya bulunamadı:** Yolun doğru olup olmadığını teyit etmesini iste.
- **İzin reddedildi:** Dosyaya okuma izninin olmadığını bildir.
