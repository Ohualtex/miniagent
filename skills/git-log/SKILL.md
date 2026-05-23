---
name: git-log
version: 0.1.0
description: Bir Git reposundaki son commit'leri özetler. git CLI gerekir.
icon: "🌳"
example_prompt: "Bu repoda son commit'ler neler?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: false
tags: [git, dev, info]
---

# Git Log Skill

Bir Git reposundaki son commit geçmişini görmek için `git log` komutunu kullan.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
git -C <dizin> log --oneline --graph --decorate -20
```

`<dizin>` yerine kullanıcının belirttiği dizini koy. Kullanıcı dizin belirtmezse
`.` (mevcut dizin) kullan.

Eğer kullanıcı belirli bir dosyanın geçmişini istiyorsa:

```
git -C <dizin> log --oneline -10 -- <dosya>
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar.
Commit hash'lerini, mesajlarını ve varsa branch/tag bilgilerini düzenli bir
liste halinde sun.

## Hata durumları

- **Git reposu değil:** "fatal: not a git repository" hatası gelirse dizinin bir
  Git deposu olmadığını söyle.
- **`git` bulunamadı:** Git CLI'nin kurulu olmadığını bildir.
- **Boş geçmiş:** Henüz commit yoksa bunu kullanıcıya açıkla.
