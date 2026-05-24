---
name: whois
version: 0.1.0
description: Bir domain için WHOIS kayıt bilgisini (sahip, kayıt tarihi, nameserver vb.) getirir.
icon: "🔎"
example_prompt: "anthropic.com'un WHOIS bilgisi nedir?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, network_read]
network:
  allowed_domains: ["*"]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [whois]
  internet: true
tags: [whois, domain, network]
---

# WHOIS Skill

Bir domain'in kayıt bilgilerini (registrar, kayıt/yenileme tarihleri,
nameserver'lar, durum, varsa sahip bilgisi) sorgulamak için `whois` kullanılır.

## Çalıştırılacak komut

```
whois <domain>
```

`<domain>` yerine kullanıcının verdiği domain'i koy.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile özetle.
WHOIS çıktısı çok uzun olabilir; en faydalı alanları öne çıkar:
- **Registrar** (kayıt kuruluşu)
- **Created / Registry Expiry Date** (kayıt ve yenileme tarihleri)
- **Name Server** (nameserver listesi)
- **Status** (`clientTransferProhibited` vb. domain durum kodları)
- **Registrant** (genelde gizlilik koruması nedeniyle `REDACTED`)

## Hata durumları

- **`No match for ...`:** Domain kayıtlı değil.
- **Boş veya çok kısa çıktı:** Bazı TLD'lerin (özellikle yeni TLD'lerin) WHOIS
  sunucuları minimal bilgi verir; kullanıcıya bunu söyle.
- **`whois` bulunamadı:** macOS'ta önyüklüdür; Linux'ta `whois` paketinin
  kurulması gerekir (`apt install whois` veya `dnf install whois`).
- **Rate limit:** Bazı WHOIS sunucuları sık sorguları reddeder; biraz beklemek
  gerekebilir.
