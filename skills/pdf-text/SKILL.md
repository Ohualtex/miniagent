---
name: pdf-text
version: 0.1.0
description: Bir PDF dosyasından düz metni çıkarır (poppler-utils ile).
icon: "📄"
example_prompt: "Şu PDF'in metnini çıkar: ~/Documents/rapor.pdf"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [pdftotext]
  internet: false
tags: [pdf, text, extract, file]
---

# PDF Text Skill

Bir PDF dosyasından düz metni çıkarmak için `pdftotext` (poppler-utils
paketi) kullanılır.

## Çalıştırılacak komut

**Tüm metni stdout'a:**

```
pdftotext <dosya.pdf> -
```

Sondaki `-` çıktıyı stdout'a yönlendirir.

**Belirli sayfa aralığı (örn. 1-3):**

```
pdftotext -f 1 -l 3 <dosya.pdf> -
```

**Düzen koruyarak (sütun yapısı):**

```
pdftotext -layout <dosya.pdf> -
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Çıktı çok uzunsa ilk birkaç paragrafı göster, sonra "tamamını ister misin?"
  diye sor
- PDF tarama (görsel) ise metin gelmeyebilir; bu durumda OCR (Tesseract vb.)
  gerek olduğunu söyle

## Hata durumları

- **`pdftotext` bulunamadı:** macOS'ta `brew install poppler`, Linux'ta
  `apt install poppler-utils` veya `dnf install poppler-utils`.
- **`Syntax Error`:** Bozuk veya şifreli PDF; şifreliyse `-upw <sifre>`
  kullanılabilir.
- **Boş çıktı:** PDF taranmış olabilir (görsel); OCR gerek.
