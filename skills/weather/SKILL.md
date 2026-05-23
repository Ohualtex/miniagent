---
name: weather
version: 0.1.0
description: Bir şehrin güncel hava durumunu söyler. İnternet bağlantısı ve curl gerekir.
icon: "🌤️"
example_prompt: "İstanbul'da hava nasıl?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, network_read]
network:
  allowed_domains: [wttr.in]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [curl]
  internet: true
tags: [weather, info, network]
---

# Weather Skill

Bir şehrin güncel hava durumunu öğrenmek için **wttr.in** servisini kullan.
API anahtarı veya hesap gerektirmez.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
curl -s 'https://wttr.in/<şehir>?format=3'
```

`<şehir>` yerine kullanıcının söylediği şehri koy. Şehir adında Türkçe karakter
olursa İngilizce karşılığını kullan (*İstanbul → Istanbul*).

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar.
Sıcaklığı, hava koşulunu (güneşli/yağmurlu/karlı vs.) öne çıkar.

## Hata durumları

- **Boş/eksik çıktı veya bağlantı hatası:** İnternet erişimi olmayabilir ya da
  `wttr.in` geçici olarak yanıt vermiyordur; kullanıcıya tekrar denemesini söyle.
- **Bilinmeyen şehir:** Servis konumu bulamazsa şehir adını İngilizce yazmayı
  öner (*İstanbul → Istanbul*).
- **`curl` bulunamadı:** `curl`'ün kurulu olmadığını bildir.
