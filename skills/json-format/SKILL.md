---
name: json-format
version: 0.1.0
description: JSON dosyalarını güzel formatlı (pretty-print) gösterir veya geçerliliğini kontrol eder.
icon: "🧾"
example_prompt: "Şu config.json dosyasını düzgün formatla göster"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_read]
author:
  name: Yıldırım Özal
  github: yildirimozal
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [python3]
  internet: false
tags: [json, format, dev]
---

# JSON Format Skill

Kullanıcının belirttiği JSON dosyasını güzel formatlı olarak göstermek veya
geçerliliğini doğrulamak için Python'un yerleşik `json.tool` modülünü kullan.

## Çalıştırılacak komut

**Dosyadan okuma ve formatlama:**

`bash` tool'u ile şunu çalıştır:

```
python3 -m json.tool <dosya_yolu>
```

`<dosya_yolu>` yerine kullanıcının belirttiği dosya yolunu koy. `~` desteklenir.

**Eğer kullanıcı doğrudan JSON metni yapıştırdıysa:**

```
echo '<json_metni>' | python3 -m json.tool
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- **Başarılı** ise: formatlı JSON çıktısını göster ve "JSON geçerli" de.
- **Hata** varsa: hatanın ne olduğunu Türkçe açıkla (eksik virgül, kapanmamış
  parantez vb.).

## Hata durumları

- **Geçersiz JSON:** `json.tool` `Expecting ...` hatası döndürür; satır/sütun
  bilgisini kullanarak sorunu Türkçe açıkla.
- **Dosya bulunamadı:** Verilen yol yoksa kullanıcıdan yolu teyit etmesini iste.
- **`python3` bulunamadı:** Python 3'ün kurulu olmadığını bildir.
