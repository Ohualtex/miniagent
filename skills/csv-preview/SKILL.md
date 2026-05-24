---
name: csv-preview
version: 0.1.0
description: Bir CSV dosyasının ilk N satırını sütun hizalanmış şekilde gösterir.
icon: "📑"
example_prompt: "data.csv dosyasının ilk 10 satırı"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [head, column]
  internet: false
tags: [csv, data, preview, file]
---

# CSV Preview Skill

Bir CSV dosyasının ilk N satırını sütun hizalanmış (okunaklı) bir tablo
hâlinde göstermek için `head` + `column` borusu kullanılır.

## Çalıştırılacak komut

**Varsayılan (ilk 10 satır):**

```
head -10 <dosya.csv> | column -t -s,
```

**N satır:**

```
head -<N> <dosya.csv> | column -t -s,
```

**Eğer ayraç virgül değilse:**
- Tab: `column -t -s$'\t'`
- Noktalı virgül: `column -t -s';'`

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- İlk satır başlık olarak değerlendirilebilir; sütun adlarını öne çıkar
- Toplam satır sayısı için `wc -l <dosya>` çağırılabilir (kullanıcı isterse)
- Sütun değerlerinde virgül varsa (alıntılı CSV) `column` doğru parse etmez;
  bu durumu kullanıcıya bildir ve gerekirse `python3 -c "import csv,sys; ..."`
  ile doğru parse öner

## Hata durumları

- **Dosya bulunamadı:** Yolu teyit et.
- **Boş dosya:** Çıktı boş gelir; kullanıcıya dosyanın boş olduğunu söyle.
- **`column` bulunamadı:** Linux'ta `util-linux` paketi; macOS'ta önyüklü.
