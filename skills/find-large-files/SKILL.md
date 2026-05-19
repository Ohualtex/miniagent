---
name: find-large-files
description: Bir klasördeki en büyük dosyaları/alt klasörleri bulur.
---

# Find Large Files Skill

Bir klasörde yer kaplayan en büyük öğeleri bulmak için `du` kullan.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
du -ah <klasör> 2>/dev/null | sort -hr | head -10
```

`<klasör>` yerine kullanıcının söylediği yolu koy (örn: `~/Downloads`, `~/Desktop`).

## Sonuç geldikten sonra

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar.
En büyük 3-5 öğeyi öne çıkar. Silme komutu **ASLA çalıştırma**.
