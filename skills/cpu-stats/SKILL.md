---
name: cpu-stats
version: 0.1.0
description: Sistemin yük ortalamasını (load average) ve uptime'ı gösterir.
icon: "🧮"
example_prompt: "Sistemin yükü ne durumda?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [uptime]
  internet: false
tags: [cpu, load, system]
---

# CPU Stats Skill

Sistemin yük ortalamasını (1/5/15 dakika) ve ne kadar süredir açık olduğunu
görmek için `uptime` kullanılır. Hem macOS hem Linux'ta yerleşiktir.

Süreç bazlı CPU kullanımı için `process-top` skill'ini kullan.

## Çalıştırılacak komut

```
uptime
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar.
`uptime` çıktısı şu formattadır:

```
22:14  up 3 days, 4:32, 2 users, load averages: 1.23 0.98 1.05
```

- **Uptime** (sistem ne kadar süredir açık) bilgisini öne çıkar
- **Load average** (1, 5, 15 dakika) değerlerini yorumla:
  - 1.0 değer 1 çekirdeği tam yükler
  - 8 çekirdekli sistemde 8.0 = tam yük
  - Değer çekirdek sayısının üstündeyse sistem aşırı yüklü demektir

## Hata durumları

- **`uptime` bulunamadı:** Çok nadirdir; sistem core utilities eksik olabilir.
