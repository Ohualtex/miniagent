---
name: archive-list
version: 0.1.0
description: Bir zip, tar veya tar.gz arşivinin içeriğini listeler (içeriği çıkarmadan).
icon: "📦"
example_prompt: "Bu zip'in içinde neler var: ~/Downloads/proje.zip"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [unzip, tar]
  internet: false
tags: [archive, zip, tar, file]
---

# Archive List Skill

Bir arşiv dosyasının içeriğini (çıkarmadan) listelemek için arşiv tipine göre
`unzip` veya `tar` kullanılır.

## Çalıştırılacak komut

**zip için:**

```
unzip -l <arsiv>
```

**tar / tar.gz / tar.bz2 için:**

```
tar -tvf <arsiv>
```

Yeni `tar` sürümleri sıkıştırma tipini otomatik tanır. Eski sürümlerde:
`.tar.gz` için `tar -tzvf`, `.tar.bz2` için `tar -tjvf`.

Dosya uzantısına göre uygun komutu seç.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Dosya/dizin **sayısını** öne çıkar
- Toplam (açılmış) **boyutu** göster
- Çok sayıda dosya varsa ilk birkaçını listeleyip "daha fazlası var" de

## Hata durumları

- **`cannot find or open`:** Dosya yolu yanlış veya dosya yok.
- **`not a valid archive`:** Bozuk veya eksik arşiv dosyası.
- **`unzip`/`tar` bulunamadı:** Hemen her sistemde vardır; yoksa kurulması gerek.
