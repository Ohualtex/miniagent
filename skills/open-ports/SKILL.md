---
name: open-ports
description: Makinedeki açık portları ve bunları dinleyen süreçleri listeler.
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

## Sonuç geldikten sonra

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar.
Her açık port için şunları belirt:
- **Port numarası**
- **Dinleyen süreç adı** (PID dahil)
- **Protokol** (TCP)

Önemli servisleri vurgula (örn. 80=HTTP, 443=HTTPS, 3000=dev server,
5432=PostgreSQL, 8080=proxy vb.).
