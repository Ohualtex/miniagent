---
name: git-status
version: 0.1.0
description: Bir Git reposundaki çalışma ağacının kısa durumunu ve branch bilgisini gösterir.
icon: "📋"
example_prompt: "Bu repoda neler değişmiş?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: false
tags: [git, status, vcs]
---

# Git Status Skill

Bir Git reposundaki çalışma ağacının durumunu (değişen, staged, untracked
dosyalar) ve branch bilgisini görmek için `git status` kısa formu kullanılır.

## Çalıştırılacak komut

```
git -C <dizin> status -sb
```

`<dizin>` yerine kullanıcının belirttiği dizini koy. Kullanıcı dizin
belirtmezse `.` (mevcut dizin) kullan.

`-sb` bayrağı **short format + branch** demektir — kısa satır başına bir
dosya, üst satırda branch bilgisi.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar.
Kısa formatta her satır iki karakterle başlar:
- ` M` → working tree'de değişmiş (staged değil)
- `M ` → staged
- `MM` → hem staged hem working tree'de değişmiş
- `A ` → staged eklenmiş (yeni)
- `D ` → staged silinmiş
- `??` → izlenmiyor (untracked)

Branch satırı `## branch...origin/branch [ahead N, behind M]` formatında gelir;
varsa "ahead/behind" bilgisini açıkça söyle.

## Hata durumları

- **`not a git repository`:** Verilen dizin bir Git reposu değil.
- **Dizin bulunamadı:** Yolun doğru olup olmadığını teyit et.
- **`git` bulunamadı:** Git kurulu değil.
