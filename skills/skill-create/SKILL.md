---
name: skill-create
version: 0.1.0
description: Yeni bir skill iskeleti oluşturur (Ajanox Skill Spec v1.0 uyumlu minimal SKILL.md).
icon: "🪄"
example_prompt: "weather adlı yeni bir skill iskeleti oluştur"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  internet: false
tags: [skill, scaffold, meta, dev]
---

# Skill Create Skill

Yeni bir skill için Ajanox Skill Spec v1.0 uyumlu minimal `SKILL.md` iskeleti
oluştur. Klasör + dosya yazılır; içerik kullanıcıdan alınan veya makul
varsayılan değerlerle doldurulur.

## Çalıştırılacak komut

**1. Skill adını doğrula:**

Skill adı sadece küçük harf, rakam ve tire olmalı (örn. `git-stash`,
`pdf-merge`). Başında veya sonunda tire olmasın.

**2. Klasörü oluştur:**

```
mkdir -p skills/<skill-adi>
```

`skills/<skill-adi>` zaten varsa kullanıcıya sor (içindeki SKILL.md
üzerine yazılır mı?).

**3. SKILL.md'yi heredoc ile yaz:**

```
cat > skills/<skill-adi>/SKILL.md <<'EOF'
---
name: <skill-adi>
version: 0.1.0
description: <kısa açıklama>
icon: "🔧"
example_prompt: "<örnek kullanıcı isteği>"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
license: MIT
language: tr
languages: [tr, en]
requires:
  internet: false
tags: [<etiket>]
---

# <Skill Başlığı>

Skill'in ne yaptığını ve hangi CLI aracını kullandığını açıkla.

## Çalıştırılacak komut

`bash` tool'u ile şunu çalıştır:

```
<komut>
```

## Sonuç işleme

Agent çıktıyı kullanıcıya nasıl sunacağını açıkla.

## Hata durumları

Olası hata durumlarını ve nasıl raporlanacağını açıkla.
EOF
```

Description, example_prompt, tags, komut gibi placeholder'ları kullanıcının
verdiği bilgilere göre doldur.

**Ağ kullanan skill için**: `permissions`'a `network_read` ekle, frontmatter'a
`network:\n  allowed_domains: [<domain>]` bloğu koy, `requires.internet: true`
yap.

**Dosya yazan skill için**: `permissions`'a `file_write` ekle.

## Sonuç işleme

Kullanıcıya:
- Klasörün ve SKILL.md'nin oluşturulduğunu onayla
- Dosyanın yolunu ver: `skills/<skill-adi>/SKILL.md`
- "Şimdi içeriği geliştir, sonra `ajanox skill check skills/<skill-adi>` ile
  doğrula" diye yönlendir

## Hata durumları

- **Skill klasörü zaten var:** Mevcut SKILL.md varsa onay olmadan üzerine YAZMA.
- **Geçersiz skill adı:** Sadece küçük harf, rakam ve tire kullan;
  başında/sonunda tire olmasın.
