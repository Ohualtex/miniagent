---
name: git-diff
version: 0.1.0
description: Bir Git reposundaki working tree veya staged değişiklikleri gösterir.
icon: "🔀"
example_prompt: "Bu repoda staged olmayan değişiklikleri göster"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [git]
  internet: false
tags: [git, diff, vcs]
---

# Git Diff Skill

Bir Git reposundaki working tree veya staged değişiklikleri görmek için
`git diff` kullanılır.

## Çalıştırılacak komut

**Working tree değişiklikleri (staged değil):**

```
git -C <dizin> diff
```

**Staged değişiklikler:**

```
git -C <dizin> diff --cached
```

**Belirli bir dosya için:**

```
git -C <dizin> diff -- <dosya>
```

**Sadece istatistik (hangi dosyalar ne kadar değişti):**

```
git -C <dizin> diff --stat
```

`<dizin>` yerine kullanıcının belirttiği dizini koy. Belirtmezse `.` kullan.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- Çıktı çok uzunsa önce `--stat` ile özet ver, sonra "tam diff ister misin?" diye sor
- `+` satırlar eklenen, `-` satırlar silinen kod
- Her dosya için `diff --git a/... b/...` başlığını öne çıkar

## Hata durumları

- **`not a git repository`:** Verilen dizin bir Git reposu değil.
- **Çıktı boş:** Değişiklik yoksa diff boş gelir; kullanıcıya "değişiklik yok" de.
- **Dizin bulunamadı:** Yolu teyit et.
