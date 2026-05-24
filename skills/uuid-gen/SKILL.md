---
name: uuid-gen
version: 0.1.0
description: Rastgele bir UUID (v4) üretir; benzersiz tanımlayıcı gerektiğinde kullanılır.
icon: "🆔"
example_prompt: "Bana 3 tane UUID üret"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [uuidgen]
  internet: false
tags: [uuid, identifier, dev]
---

# UUID Gen Skill

Benzersiz tanımlayıcı (UUID v4) üretmek için sistem aracı `uuidgen` kullanılır.
Hem macOS hem Linux'ta yerleşiktir.

## Çalıştırılacak komut

**Tek UUID:**

```
uuidgen
```

**Birden fazla UUID (örn. 5 tane):**

```
for i in $(seq 5); do uuidgen; done
```

`seq` ardından gelen sayıyı kullanıcının isteğine göre değiştir.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya net biçimde aktar:
- UUID'leri satır satır göster
- macOS'ta varsayılan büyük harfli (`uppercase`) gelir; kullanıcı küçük
  harf isterse `tr '[:upper:]' '[:lower:]'` borusu ile çevir

## Hata durumları

- **`uuidgen` bulunamadı:** Çok nadirdir; Python fallback olarak şu
  kullanılabilir: `python3 -c 'import uuid; print(uuid.uuid4())'`.
