---
name: mac-notification
description: macOS'ta masaüstü bildirimi gösterir. Sadece Mac'te çalışır.
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

## Sonuç geldikten sonra

`osascript` başarılı olunca çıktı dönmez (boş string). Kullanıcıya kısa bir
onay ver:

> Bildirim gönderildi: "[mesaj]"

Sadece macOS'ta çalışır. Linux/Windows kullanıcısına "bu skill Mac'e özel"
olduğunu söyle.
