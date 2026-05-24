---
name: image-info
version: 0.1.0
description: Bir görsel dosyanın boyut, format ve metadata bilgisini gösterir.
icon: "🖼️"
example_prompt: "~/Desktop/foto.jpg'in çözünürlüğü ne?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [sips]
  internet: false
tags: [image, metadata, file]
---

# Image Info Skill

Bir görselin boyut, format ve temel metadata bilgisini görmek için platform
araçları kullanılır.

## Çalıştırılacak komut

**macOS:**

```
sips -g all <dosya>
```

**Linux (ImageMagick yüklüyse):**

```
identify -verbose <dosya>
```

**Cross-platform (exiftool yüklüyse — EXIF için en zengin):**

```
exiftool <dosya>
```

Önce `sips`'i dene (macOS). Hata dönerse `identify`, sonra `exiftool` dene.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile özetle:
- **Çözünürlük** (genişlik × yükseklik) ve **format** (JPEG/PNG/HEIC vb.) öne çıkar
- **Renk profili** (sRGB, Display P3 vb.)
- **Dosya boyutu**
- EXIF varsa: kamera modeli, çekim tarihi, ISO/açıklık/odak

## Hata durumları

- **Dosya bulunamadı:** Yolu teyit et.
- **`sips` bulunamadı (Linux):** ImageMagick veya exiftool kurulması gerek.
- **Geçersiz görsel:** Dosya bozuk veya görsel formatında değil.
