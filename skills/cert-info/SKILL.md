---
name: cert-info
version: 0.1.0
description: Bir HTTPS domain'inin TLS sertifika bilgilerini (subject, issuer, geçerlilik tarihleri) gösterir.
icon: "🔐"
example_prompt: "github.com'un TLS sertifikası ne zaman bitiyor?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, network_read]
network:
  allowed_domains: ["*"]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [openssl]
  internet: true
tags: [tls, ssl, cert, security, network]
---

# Cert Info Skill

Bir HTTPS domain'inin TLS/SSL sertifikasının özetini (subject, issuer,
geçerlilik tarihleri) görmek için `openssl s_client` ve `openssl x509`
zinciri kullanılır.

## Çalıştırılacak komut

```
echo | openssl s_client -servername <domain> -connect <domain>:443 2>/dev/null | openssl x509 -noout -subject -issuer -dates
```

`<domain>` yerine kullanıcının verdiği host adını koy (örn. `github.com`).
Port varsayılan 443; farklı port istenirse iki yerde de değiştir
(örn. `:8443`).

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- **subject** → sertifikanın hangi domain için verildiği (Common Name)
- **issuer** → sertifikayı veren CA (Let's Encrypt, DigiCert, Sectigo vb.)
- **notBefore / notAfter** → geçerlilik başlangıç ve bitiş tarihleri
- **Bitime kaç gün kaldığını** hesaplayıp söyle
- Bitime az kalmışsa (örn. < 30 gün) açıkça uyar

## Hata durumları

- **`Connection refused` / timeout:** Host 443 portunda HTTPS dinlemiyor.
- **`unable to get local issuer certificate`:** Bağlantı kuruldu ama
  zincir doğrulaması başarısız — yine de subject/issuer bilgisi alınabilir.
- **`openssl` bulunamadı:** Hemen her sistemde vardır; yoksa kurulması gerek.
- **Self-signed certificate:** Sertifika kendi tarafından imzalanmış;
  kullanıcıya bunun bir uyarı olduğunu (ama hata olmadığını) belirt.
