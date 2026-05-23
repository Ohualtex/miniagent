---
name: dns-lookup
version: 0.1.0
description: Bir domain için DNS sorgusu çalıştırır (A, AAAA, MX, TXT, NS, CNAME kayıtları).
icon: "🌐"
example_prompt: "anthropic.com'un DNS A kayıtları neler?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, network_read]
network:
  allowed_domains: ["*"]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [dig]
  internet: true
tags: [dns, network, domain]
---

# DNS Lookup Skill

Bir domain için DNS kayıtlarını sorgulamak üzere `dig` kullanılır.
A (IPv4), AAAA (IPv6), MX (mail), TXT, NS (nameserver), CNAME kayıtları için.

## Çalıştırılacak komut

**Varsayılan (A kaydı):**

```
dig +short <domain>
```

**Belirli kayıt tipi:**

```
dig +short <domain> <kayit_tipi>
```

`<kayit_tipi>` yerine `A`, `AAAA`, `MX`, `TXT`, `NS`, `CNAME` koy.

**Bir özet için tüm kayıtlar:**

```
dig +short <domain> ANY
```

Kullanıcı hangi tipi istediyse onu kullan. Belirsizse `A` ile başla.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar:
- Kayıt değerlerini liste hâlinde göster
- MX kayıtları için öncelik (priority) bilgisini belirt
- Çıktıda IP varsa, IPv4 mü IPv6 mı olduğunu söyle

## Hata durumları

- **Boş çıktı:** Domain bu tip kayda sahip değildir; başka bir tip denemeyi
  öner (ör. A yoksa AAAA).
- **`dig` bulunamadı:** macOS'ta önyüklüdür; Linux'ta `dnsutils` (Debian/
  Ubuntu) veya `bind-utils` (RHEL/Fedora) paketinin kurulması gerekir.
- **`SERVFAIL` / `NXDOMAIN`:** Domain yok veya nameserver yanıt vermiyor;
  yazımı kontrol etmesini iste.
