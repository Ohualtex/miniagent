---
name: ip-location
version: 0.1.0
description: Public IP adresini ve coğrafi konum bilgisini gösterir. İnternet bağlantısı ve curl gerekir.
icon: "🌍"
example_prompt: "IP adresim nerede görünüyor?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, network_read]
network:
  allowed_domains: [ipinfo.io]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [curl]
  internet: true
tags: [network, ip, geo, info]
---

# IP Location Skill

Kullanıcının public IP adresini ve bu IP'ye bağlı coğrafi konum bilgisini
öğrenmek için ücretsiz bir API kullan.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
curl -s https://ipinfo.io
```

Bu komut JSON formatında IP, şehir, bölge, ülke, koordinat ve ISP bilgisi
döndürür.

## Sonuç işleme

`bash` tool'undan gelen gerçek JSON çıktısını **doğal Türkçe** ile kullanıcıya
aktar. Şu bilgileri vurgula:
- **IP adresi**
- **Konum** (şehir, bölge, ülke)
- **ISP / Organizasyon**
- **Koordinatlar** (isteğe bağlı)

Ham JSON'u yapıştırma, okunaklı biçimde sun.

## Hata durumları

- **Boş çıktı / bağlantı hatası:** İnternet erişimi yoksa ya da `ipinfo.io`
  yanıt vermiyorsa kullanıcıya tekrar denemesini söyle.
- **Hız limiti (rate limit):** Çok sık istek atılırsa servis kısıtlama
  döndürebilir; bir süre sonra tekrar denenmesini öner.
- **`curl` bulunamadı:** `curl`'ün kurulu olmadığını bildir.
