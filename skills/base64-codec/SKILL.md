---
name: base64-codec
version: 0.1.0
description: Metni veya dosyayı base64 ile encode/decode eder.
icon: "🔁"
example_prompt: "Bu base64'ü çözer misin: SGVsbG8gd29ybGQ="
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [base64]
  internet: false
tags: [base64, encode, decode, dev]
---

# Base64 Codec Skill

Metin veya dosyayı base64 ile encode/decode etmek için sistem aracı `base64`
kullanılır. Hem macOS hem Linux'ta yerleşiktir.

## Çalıştırılacak komut

**Decode (base64 → metin)** — base64 metni shell-safe karakterlerden
(`A-Za-z0-9+/=`) oluştuğu için doğrudan kullanılabilir:

```
echo '<base64_metni>' | base64 -d
```

**Encode (dosya → base64):**

macOS:
```
base64 -i <dosya_yolu>
```

Linux:
```
base64 <dosya_yolu>
```

**Encode (kullanıcının yapıştırdığı arbitrary metin):**

`echo '<metin>' | base64` **kullanma** — metin içinde tek tırnak veya shell
özel karakterleri varsa komut kırılır. Bunun yerine kullanıcıdan metni
geçici bir dosyaya kaydetmesini iste (örn. `~/in.txt`) ve sonra
`base64 -i ~/in.txt` (macOS) ya da `base64 ~/in.txt` (Linux) çalıştır.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- **Decode**: çözülen metni göster
- **Encode**: base64 çıktısını göster; çok uzunsa ilk birkaç satırını ver

## Hata durumları

- **`invalid input`:** Kullanıcının verdiği base64 bozuk; padding (`=`)
  eksik olabilir veya geçersiz karakter içeriyor.
- **Dosya bulunamadı:** Yolun doğru olup olmadığını teyit et.
- **`base64` bulunamadı:** Çok nadirdir; `coreutils` paketinin kurulu
  olması gerekir.
