---
name: date-calc
version: 0.1.0
description: Tarih aritmetiği yapar (N gün/ay sonra/önce ne tarih, formatlama vb.).
icon: "📅"
example_prompt: "Bugünden 90 gün sonra hangi tarih?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [date]
  internet: false
tags: [date, time, calculation]
---

# Date Calc Skill

Tarih aritmetiği için `date` komutu kullanılır. macOS'ta BSD `date`,
Linux'ta GNU `date` farklı sözdizimi kullanır.

## Çalıştırılacak komut

**Şimdi:**

```
date
```

**N gün sonra:**
- macOS: `date -v +<N>d`
- Linux: `date -d "+<N> days"`

**Belirli formatlama (ISO):**
- macOS: `date -v +<N>d +"%Y-%m-%d"`
- Linux: `date -d "+<N> days" +"%Y-%m-%d"`

**Geçmiş tarih:**
- macOS: `date -v -<N>d`
- Linux: `date -d "-<N> days"`

Önce macOS varyantını dene; `illegal option` hatası dönerse Linux varyantına geç.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- İstenen tarihi belirgin biçimde göster
- Gerekirse haftanın gününü de söyle

## Hata durumları

- **`illegal option -- v`:** GNU date kullanıyorsun (Linux); `-d "+N days"`
  formatına geç.
- **`invalid date`:** Tarih dizesi parse edilemedi; format kontrol.
