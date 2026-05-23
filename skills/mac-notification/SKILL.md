---
name: mac-notification
version: 0.1.0
description: macOS'ta masaüstü bildirimi gösterir. Sadece Mac'te çalışır.
icon: "🔔"
example_prompt: "Bana 'mola zamanı' diye bir bildirim gönder"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, notification]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  os: [darwin]
  binaries: [osascript]
  internet: false
tags: [notification, macos, info]
---

# Mac Notification Skill

macOS'un yerleşik bildirim sistemini kullanarak kullanıcıya bir bildirim göster.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
osascript -e 'display notification "MESAJ" with title "BAŞLIK"'
```

`MESAJ` ve `BAŞLIK` yerine kullanıcının istediği metinleri koy. Mesajda
apostrof varsa kaçırmayı unutma.

## Sonuç işleme

`osascript` başarılı olunca çıktı dönmez (boş string). Kullanıcıya kısa bir
onay ver:

> Bildirim gönderildi: "[mesaj]"

## Hata durumları

- **macOS değil:** Linux/Windows kullanıcısına bu skill'in Mac'e özel olduğunu
  söyle (`osascript` yalnızca macOS'ta bulunur).
- **`osascript` bulunamadı:** macOS dışı bir ortamda çalıştırılmış olabilir;
  uyumlu olmadığını bildir.
- **Apostrof/kaçış hatası:** Mesaj veya başlıkta tırnak varsa komutun
  bozulabileceğini unutma; metni düzgün kaçır.
