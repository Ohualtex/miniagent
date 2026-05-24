---
name: process-top
version: 0.1.0
description: CPU veya belleğe göre en aktif süreçleri listeler.
icon: "⚡"
example_prompt: "En çok CPU kullanan süreçler hangileri?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [ps]
  internet: false
tags: [process, system, monitoring]
---

# Process Top Skill

Hangi süreçlerin sistem kaynaklarını (CPU, RAM) tükettiğini görmek için
`ps` kullanılır. Hem macOS'ta hem Linux'ta çalışır.

## Çalıştırılacak komut

**CPU'ya göre en aktif 10 süreç:**

```
ps -A -o pid,user,%cpu,%mem,comm | sort -k3 -nr | head -10
```

**Belleğe göre en aktif 10 süreç:**

```
ps -A -o pid,user,%cpu,%mem,comm | sort -k4 -nr | head -10
```

Kullanıcı hangisini istediyse onu çalıştır. Belirsizse varsayılan olarak
CPU'ya göre listele.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar:
- Her süreç için **PID**, **kullanıcı**, **CPU%**, **MEM%**, **komut adı**
  bilgisini ver
- En yüksek 3 süreci öne çıkar
- Çıktının başlık satırını koru, okunaklı bir tablo gibi sun

## Hata durumları

- **`ps` bulunamadı:** Çok nadirdir; sistem core utilities eksik olabilir.
- **Çıktı boş:** Sıralama veya boru hattında sorun olabilir; ham `ps -A`
  çıktısının geldiğini doğrula.
