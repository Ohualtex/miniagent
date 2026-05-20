---
name: ip-location
description: Public IP adresini ve coğrafi konum bilgisini gösterir. İnternet bağlantısı ve curl gerekir.
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

## Sonuç geldikten sonra

`bash` tool'undan gelen gerçek JSON çıktısını **doğal Türkçe** ile kullanıcıya
aktar. Şu bilgileri vurgula:
- **IP adresi**
- **Konum** (şehir, bölge, ülke)
- **ISP / Organizasyon**
- **Koordinatlar** (isteğe bağlı)

Ham JSON'u yapıştırma, okunaklı biçimde sun.
