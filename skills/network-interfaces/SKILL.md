---
name: network-interfaces
version: 0.1.0
description: Yerel ağ arabirimlerini ve IP adreslerini listeler.
icon: "🔌"
example_prompt: "Hangi network interface'lere bağlıyım?"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [ifconfig]
  internet: false
tags: [network, interface, system]
---

# Network Interfaces Skill

Yerel ağ arabirimlerini (Ethernet, Wi-Fi, loopback) ve atanan IP adreslerini
görmek için `ifconfig` (macOS, Linux) veya `ip addr` (modern Linux) kullanılır.

## Çalıştırılacak komut

**Cross-platform (ifconfig):**

```
ifconfig
```

**Modern Linux alternatifi:**

```
ip addr
```

`ifconfig` yoksa `ip addr` dene.

## Sonuç işleme

`bash` tool'undan gelen gerçek çıktıyı kullanıcıya **doğal Türkçe** ile özetle:
- Aktif arabirimleri (`UP` flag'i veya `state UP`) öne çıkar
- Her aktif arabirim için **IPv4** (`inet`) ve **IPv6** (`inet6`) adreslerini ver
- **MAC adresi** (`ether` / `link/ether`) bilgisini de ekleyebilirsin
- Loopback (`lo` / `lo0`) gerekmiyorsa listeleme dışına alınabilir

## Hata durumları

- **`ifconfig` bulunamadı:** Modern Linux'ta `net-tools` yüklü değil olabilir;
  `ip addr` denenmeli.
- **Çıktı boş:** Çok nadirdir; ağ alt sistemi sorunlu olabilir.
