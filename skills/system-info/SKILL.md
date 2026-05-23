---
name: system-info
version: 0.1.0
description: Makine hakkında detaylı sistem bilgisi verir (OS, CPU, RAM, disk).
icon: "🖥️"
example_prompt: "Sistemim hakkında bilgi ver"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, system_info]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  os: [linux, darwin, wsl]
  binaries: [uname, df]
  internet: false
tags: [system, hardware, info]
---

# System Info Skill

Kullanıcının makinesi hakkında detaylı bilgi toplamak için sistem komutlarını
kullan.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
echo "=== OS ===" && uname -a && echo "" && echo "=== Disk ===" && df -h / && echo "" && echo "=== Bellek ===" && vm_stat 2>/dev/null || free -h 2>/dev/null && echo "" && echo "=== CPU ===" && sysctl -n machdep.cpu.brand_string 2>/dev/null || lscpu 2>/dev/null | head -5
```

Bu komut hem macOS hem Linux'ta çalışır. İlk başarılı olan komutu kullanır.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar.
İşletim sistemi, CPU modeli, toplam/kullanılan RAM ve disk alanını okunaklı bir
tablo veya liste halinde sun. Ham çıktıyı doğrudan yapıştırma, yorumla.

## Hata durumları

- **Platforma özgü komut çalışmaz:** macOS komutları (`vm_stat`,
  `sysctl ... cpu`) Linux'ta, Linux komutları (`free`, `lscpu`) macOS'ta hata
  verebilir; `||` ile diğerine geçilir, eksik bölümleri kullanıcıya bildir.
- **Boş/eksik bölüm:** İlgili araç yoksa o bilgiyi atla ve kalanları sun.
