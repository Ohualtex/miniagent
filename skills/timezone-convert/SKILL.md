---
name: timezone-convert
version: 0.1.0
description: Şu anki zamanı veya verilen bir zamanı farklı zaman dilimleri arasında çevirir.
icon: "🌍"
example_prompt: "İstanbul'da 15:00 New York'ta saat kaç?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [date]
  internet: false
tags: [time, timezone, date]
---

# Timezone Convert Skill

Zaman dilimleri arasında zaman dönüşümü için `TZ` environment değişkeni ile
`date` komutu kullanılır.

## Çalıştırılacak komut

**Hedef zaman diliminde şu anki zaman:**

```
TZ='<zone>' date
```

`<zone>` örnekleri: `Europe/Istanbul`, `America/New_York`, `Asia/Tokyo`,
`UTC`. (IANA timezone listesinden seç.)

**Belirli bir UTC zamanını hedef zaman diliminde göster (Linux):**

```
TZ='<hedef>' date -d "<YYYY-MM-DD HH:MM> UTC"
```

**macOS için:**

```
TZ='<hedef>' date -j -f "%Y-%m-%d %H:%M %z" "<YYYY-MM-DD HH:MM> +0000" "+%Y-%m-%d %H:%M %Z"
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Hedef zaman diliminin **adını** belirt
- **Yaz/kış saati** (DST) farkı varsa hatırlat (özellikle Avrupa/ABD arası)
- Türkiye TRT, Avrupa için CET/CEST, ABD doğu için EST/EDT gibi kısaltmalar
  okuyucuya yardımcı

## Hata durumları

- **`time zone not found`:** IANA zone adı yanlış; doğrusunu öner (örn.
  `Europe/Istanbul`).
- **`invalid date`:** Tarih formatı bozuk.
