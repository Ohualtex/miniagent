---
name: screen-info
version: 0.1.0
description: Bağlı ekranların çözünürlük, refresh rate ve renk derinliği bilgisini gösterir.
icon: "🖥️"
example_prompt: "Ekranımın çözünürlüğü ne?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [system_profiler]
  internet: false
tags: [display, screen, system]
---

# Screen Info Skill

Bağlı ekranların bilgisini görmek için platforma göre uygun araç kullanılır:
macOS'ta `system_profiler`, Linux'ta X11 için `xrandr`, Wayland için
`wlr-randr`.

## Çalıştırılacak komut

**macOS:**

```
system_profiler SPDisplaysDataType
```

**Linux (X11):**

```
xrandr --query
```

**Linux (Wayland):**

```
wlr-randr 2>/dev/null
```

Platforma uygun komutu dene.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile özetle:
- Her ekran için **adı**, **çözünürlük** (px), **refresh rate** (Hz) bilgisini ver
- Birden fazla ekran varsa hepsini liste hâlinde göster
- Birincil ekranı işaretle
- macOS'ta Retina çözünürlüğü "1920 x 1200 Retina" gibi gelir; etkin
  çözünürlüğün 2x'inin fiziksel piksel sayısı olduğunu açıkla

## Hata durumları

- **`system_profiler` bulunamadı (Linux):** `xrandr` veya `wlr-randr` dene.
- **`xrandr`/`wlr-randr` bulunamadı:** Display server CLI araçları yüklü değil.
- **`Cannot open display`:** SSH oturumunda `DISPLAY` değişkeni yok.
