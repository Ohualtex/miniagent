---
name: battery
version: 0.1.0
description: Pil durumunu (şarj %'si, AC bağlı mı, kalan süre) gösterir.
icon: "🔋"
example_prompt: "Pil yüzdem ne?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [pmset]
  internet: false
tags: [battery, power, system]
---

# Battery Skill

Pil ve güç durumunu görmek için platform-özel komutlar kullanılır.

## Çalıştırılacak komut

**macOS:**

```
pmset -g batt
```

**Linux:**

```
cat /sys/class/power_supply/BAT0/capacity 2>/dev/null; cat /sys/class/power_supply/BAT0/status 2>/dev/null
```

Önce `pmset` dene. Hata dönerse Linux fallback'ini kullan.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Şarj **yüzdesini** öne çıkar
- **AC adaptör** takılı mı, **şarj oluyor mu** belirt
- macOS çıktısı kalan süreyi de verir (örn. `3:24 remaining`)
- Yüzde %20'nin altındaysa kullanıcıyı uyar

## Hata durumları

- **Pil yok:** Masaüstü sistemde pil yoktur; kullanıcıya bunu söyle.
- **`pmset` bulunamadı + `/sys/class/power_supply` yok:** Sistem destekli değil.
