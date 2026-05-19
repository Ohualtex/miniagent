---
name: weather
description: Bir şehrin güncel hava durumunu söyler. İnternet bağlantısı ve curl gerekir.
---

# Weather Skill

Bir şehrin güncel hava durumunu öğrenmek için **wttr.in** servisini kullan.
API anahtarı veya hesap gerektirmez.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
curl -s 'https://wttr.in/<şehir>?format=3'
```

`<şehir>` yerine kullanıcının söylediği şehri koy. Şehir adında Türkçe karakter
olursa İngilizce karşılığını kullan (*İstanbul → Istanbul*).

## Sonuç geldikten sonra

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar.
Sıcaklığı, hava koşulunu (güneşli/yağmurlu/karlı vs.) öne çıkar.
