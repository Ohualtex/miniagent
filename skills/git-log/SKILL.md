---
name: git-log
description: Bir Git reposundaki son commit'leri özetler. git CLI gerekir.
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

## Sonuç geldikten sonra

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar.
Commit hash'lerini, mesajlarını ve varsa branch/tag bilgilerini düzenli bir
liste halinde sun.
