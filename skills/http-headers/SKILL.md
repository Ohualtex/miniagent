---
name: http-headers
version: 0.1.0
description: Bir URL'ye HEAD isteği atıp HTTP yanıt başlıklarını (status, content-type, server vb.) gösterir.
icon: "📡"
example_prompt: "https://github.com'un HTTP header'larını göster"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, network_read]
network:
  allowed_domains: ["*"]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [curl]
  internet: true
tags: [http, headers, network, debug]
---

# HTTP Headers Skill

Bir URL'ye HEAD isteği atarak HTTP yanıt başlıklarını (status code, content-type,
server, cache, redirect vb.) görmek için `curl -I` kullanılır.

## Çalıştırılacak komut

```
curl -sIL <url>
```

Bayrakların anlamı:
- `-s` — sessiz (progress bar yok)
- `-I` — sadece header'ları al (HEAD request)
- `-L` — redirect'leri takip et

Kullanıcı redirect'leri takip etmek istemiyorsa `-L`'yi çıkar.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- **HTTP/x.x status** kodunu öne çıkar (200 OK, 301 Redirect, 404 Not Found vb.)
- Önemli başlıkları vurgula: `Content-Type`, `Server`, `Location` (redirect varsa),
  `Cache-Control`, `Set-Cookie`
- Redirect zinciri varsa (`-L` ile birden fazla yanıt) her adımı sırasıyla göster

## Hata durumları

- **`Could not resolve host`:** DNS çözümlemesi başarısız; URL yazımını kontrol et.
- **`Connection refused`:** Sunucu portu kapalı veya erişilemiyor.
- **`SSL certificate problem`:** TLS sertifikası geçersiz; kullanıcı `curl -k`
  ile (insecure) tekrar denemeyi seçebilir ama riski belirt.
- **`curl` bulunamadı:** Hemen her sistemde vardır; yoksa kurulması gerek.
