---
name: disk-usage
version: 0.1.0
description: Tüm filesystem'ların disk kullanım özetini gösterir (boş/dolu alan, doluluk %'si).
icon: "💾"
example_prompt: "Diskimde ne kadar boş alan var?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [df]
  internet: false
tags: [disk, storage, system]
---

# Disk Usage Skill

Tüm bağlı filesystem'ların disk kullanım özetini görmek için `df` kullanılır.
Toplam, kullanılan, boş alan ve doluluk yüzdesini insan-okunabilir formatta
verir.

## Çalıştırılacak komut

**Tüm filesystem'lar için:**

```
df -h
```

**Belirli bir mount point veya yol için:**

```
df -h <yol>
```

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı **doğal Türkçe** ile kullanıcıya aktar:
- Her filesystem için **mount point**, **toplam alan**, **kullanılan**,
  **kalan** ve **doluluk %** bilgisini ver
- Doluluk %'si **%90 üzerinde olan** filesystem'ları öne çıkar ve uyar
- macOS'ta `/System/Volumes/...` gibi sistem volume'larını çok kalabalıksa
  özetleyerek sun (hepsini tek tek listeleme)

## Hata durumları

- **`df` bulunamadı:** Çok nadirdir; sistem core utilities eksik olabilir.
- **Yol bulunamadı:** Verilen yolun var olup olmadığını teyit et.
- **İzin reddedildi:** Bazı filesystem'lar root erişimi isteyebilir;
  erişilebilenleri gösterip diğerlerini "izin yok" olarak işaretle.
