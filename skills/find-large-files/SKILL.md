---
name: find-large-files
version: 0.1.0
description: Bir klasördeki en büyük dosyaları/alt klasörleri bulur.
icon: "📁"
example_prompt: "İndirilenler klasöründe en büyük dosyalar neler?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [du, sort, head]
  internet: false
tags: [files, disk, info]
---

# Find Large Files Skill

Bir klasörde yer kaplayan en büyük öğeleri bulmak için `du` kullan.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
du -ah <klasör> 2>/dev/null | sort -hr | head -10
```

`<klasör>` yerine kullanıcının söylediği yolu koy (örn: `~/Downloads`, `~/Desktop`).

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar.
En büyük 3-5 öğeyi öne çıkar. Silme komutu **ASLA çalıştırma**.

## Hata durumları

- **Klasör bulunamadı / erişim yok:** Yolun yanlış olabileceğini ya da izin
  gerektirdiğini söyle (`2>/dev/null` hataları gizler, çıktı boş gelebilir).
- **Boş çıktı:** Klasör boş olabilir veya yol geçersizdir; kullanıcıdan yolu
  teyit etmesini iste.
