---
name: file-find
version: 0.1.0
description: Belirtilen dizinde isim/desen ile dosya veya klasör arar (recursive, case-insensitive).
icon: "🔍"
example_prompt: "~/Desktop'ta 'rapor' içeren dosyaları bul"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [find]
  internet: false
tags: [find, search, file, system]
---

# File Find Skill

Bir dizin altında isim deseni ile dosya/klasör aramak için `find` kullanılır.
Recursive ve case-insensitive olarak çalışır; permission hatalarını sustur.

## Çalıştırılacak komut

**Case-insensitive dosya arama:**

```
find <dizin> -iname "<pattern>" -type f 2>/dev/null
```

**Klasör arama:**

```
find <dizin> -iname "<pattern>" -type d 2>/dev/null
```

**Dosya + klasör birlikte:**

```
find <dizin> -iname "<pattern>" 2>/dev/null
```

**Çok büyük çıktıyı limitle:**

```
find <dizin> -iname "<pattern>" 2>/dev/null | head -50
```

`<dizin>` yerine kullanıcının belirttiği yolu koy. Belirtmezse:
- `~` (kullanıcı dizini) — orta kapsamlı arama için makul varsayılan
- `.` (mevcut dizin) — proje içi arama için
- `/` (tüm sistem) — **çok uzun sürebilir**, mutlaka kullanıcıya teyit
  ettir ve `| head -50` ile sınırla

`<pattern>` yıldız (`*`) ile genişletilir: `*.md`, `rapor*`, `*config*`.
`-iname` case-insensitive yapar.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile aktar:
- Bulunan dosya **sayısını** öne çıkar
- İlk birkaç sonucu liste hâlinde göster
- 50'den fazlaysa "daha fazla sonuç var, deseni daraltabilirsin" de
- Hiç sonuç yoksa "eşleşen bulunamadı" ve deseni gözden geçirmeyi öner

## Hata durumları

- **Boş çıktı:** Eşleşme yok demektir (`2>/dev/null` ile gerçek hatalar
  da gizlenmiş olabilir).
- **`find` bulunamadı:** Çok nadirdir; sistem core utilities eksik.
- **Çok yavaş:** Arama dizini çok büyük; daha dar bir dizinden başlat.
