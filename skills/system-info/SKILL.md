---
name: system-info
description: Makine hakkında detaylı sistem bilgisi verir (OS, CPU, RAM, disk).
---

# System Info Skill

Kullanıcının makinesi hakkında detaylı bilgi toplamak için sistem komutlarını
kullan.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
echo "=== OS ===" && uname -a && echo "" && echo "=== Disk ===" && df -h / && echo "" && echo "=== Bellek ===" && vm_stat 2>/dev/null || free -h 2>/dev/null && echo "" && echo "=== CPU ===" && sysctl -n machdep.cpu.brand_string 2>/dev/null || lscpu 2>/dev/null | head -5
```

Bu komut hem macOS hem Linux'ta çalışır. İlk başarılı olan komutu kullanır.

## Sonuç geldikten sonra

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar.
İşletim sistemi, CPU modeli, toplam/kullanılan RAM ve disk alanını okunaklı bir
tablo veya liste halinde sun. Ham çıktıyı doğrudan yapıştırma, yorumla.
