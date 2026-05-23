# Katkıda Bulunma

Mini Agent'a katkıda bulunmak istediğiniz için teşekkürler! Bu proje eğitim
odaklıdır, bu yüzden açıklık ve sadelik her şeyin üstündedir.

---

## Yeni Skill Ekleme (sıfır Python)

1. `skills/` altında bir klasör oluşturun:
   ```bash
   mkdir skills/skill-adiniz
   ```
2. İçine **Ajanox Skill Spec v1.0** formatında bir `SKILL.md` ekleyin:
   ```markdown
   ---
   name: skill-adiniz
   version: 0.1.0
   description: Skill'in ne yaptığını anlatan tek satırlık açıklama.
   icon: "🔧"
   example_prompt: "Örnek bir kullanıcı isteği"
   ajanox: ">=1.0.0 <2.0.0"
   permissions: [shell_safe]
   license: MIT
   language: tr
   requires:
     internet: false
   tags: [info]
   ---

   # Skill Başlığı

   Skill'in ne yaptığını ve hangi CLI aracını kullandığını açıklayın.

   ## Çalıştırılacak komut

   `bash` tool'u ile şunu çalıştır:

       komutunuz --argümanlarla

   ## Sonuç işleme

   Agent'ın çıktıyı kullanıcıya nasıl sunacağını açıklayın.

   ## Hata durumları

   Hangi hataların olabileceğini ve nasıl raporlanacağını açıklayın.
   ```
   Zorunlu alanlar: `name`, `version`, `description`, `ajanox`, `permissions`
   (geçerli izinler arasından seçin — `sudo` yasak). Ağ kullanan skill'lerde
   `network.allowed_domains` ile domain'leri kısıtlayın.
3. Göndermeden önce spec uyumunu doğrulayın:
   ```bash
   pip install ajanox
   ajanox skill check skills/skill-adiniz
   ```
   Her PR'da CI (`.github/workflows/skills.yml`) tüm skill'leri otomatik
   kontrol eder; uyumsuz bir skill merge edilemez.
4. Agent'ı yeniden başlatın — skill'iniz katalogda otomatik görünür.

---

## `agent.py` Değişiklikleri

- **Tek dosya** ve **sıfır bağımlılık** (sadece stdlib) yapısını koruyun.
- Mevcut yorum ve docstring'lere dokunmayın.
- Mümkünse type hint ekleyin.
- Göndermeden önce `python3 agent.py` ile manuel test edin.

---

## Commit Mesajları

[Conventional Commits](https://www.conventionalcommits.org/) kullanın:

```
feat(skills): hava durumu skill'i eklendi
fix: boş bash çıktısı düzgün işleniyor
chore: cross-platform destek için .gitignore güncellendi
docs: katkı rehberi eklendi
```

---

## Pull Request'ler

- Her PR tek bir mantıksal değişiklik içersin.
- PR açıklamasında **ne** ve **neden** yazın.
- İlgili issue varsa bağlayın.
