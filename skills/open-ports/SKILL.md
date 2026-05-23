---
name: open-ports
version: 0.1.0
description: Makinedeki açık portları ve bunları dinleyen süreçleri listeler.
icon: "🔌"
example_prompt: "Bilgisayarımda hangi portlar açık?"
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
  binaries: [lsof, ss]
  internet: false
tags: [network, ports, system, info]
---

# Open Ports Skill

Makinede hangi portların açık olduğunu ve bu portları hangi süreçlerin
dinlediğini görmek için sistem araçlarını kullan.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

**macOS:**

```
lsof -iTCP -sTCP:LISTEN -nP 2>/dev/null | head -30
```

**Linux (macOS'ta lsof yoksa):**

```
ss -tlnp 2>/dev/null | head -30
```

Önce `lsof` dene. Hata dönerse `ss` komutunu kullan.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar.
Her açık port için şunları belirt:
- **Port numarası**
- **Dinleyen süreç adı** (PID dahil)
- **Protokol** (TCP)

Önemli servisleri vurgula (örn. 80=HTTP, 443=HTTPS, 3000=dev server,
5432=PostgreSQL, 8080=proxy vb.).

## Hata durumları

- **`lsof` yok:** Linux'ta `lsof` bulunmayabilir; `ss -tlnp` komutuna geç.
- **İkisi de yok / boş çıktı:** Ne `lsof` ne `ss` varsa kullanıcıya bunlardan
  birini kurmasını öner; çıktı boşsa dinlenen port olmadığını söyle.
- **Yetki kısıtı:** Süreç adı/PID görünmüyorsa komutun yükseltilmiş izin
  gerektirebileceğini belirt (ama `sudo` çalıştırma).
