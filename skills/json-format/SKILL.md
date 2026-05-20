---
name: json-format
description: JSON dosyalarını güzel formatlı (pretty-print) gösterir veya geçerliliğini kontrol eder.
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

## Sonuç geldikten sonra

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- **Başarılı** ise: formatlı JSON çıktısını göster ve "JSON geçerli" de.
- **Hata** varsa: hatanın ne olduğunu Türkçe açıkla (eksik virgül, kapanmamış
  parantez vb.).
