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

`echo '<json>' | python3 -m json.tool` **kullanma** — JSON içinde tek tırnak
veya shell özel karakterleri varsa komut kırılır ve injection riski doğar.
Bunun yerine kullanıcıdan metni geçici bir dosyaya kaydetmesini iste (örn.
`~/in.json`) ve sonra dosya yoluyla `python3 -m json.tool ~/in.json` çalıştır.

## Sonuç geldikten sonra

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya aktar:
- **Başarılı** ise: formatlı JSON çıktısını göster ve "JSON geçerli" de.
- **Hata** varsa: hatanın ne olduğunu Türkçe açıkla (eksik virgül, kapanmamış
  parantez vb.).
