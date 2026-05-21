# Katkıda Bulunma

Mini Agent'a katkıda bulunmak istediğiniz için teşekkürler! Bu proje eğitim
odaklıdır, bu yüzden açıklık ve sadelik her şeyin üstündedir.

---

## Yeni Skill Ekleme (sıfır Python)

1. `skills/` altında bir klasör oluşturun:
   ```bash
   mkdir skills/skill-adiniz
   ```
2. İçine şu yapıda bir `SKILL.md` ekleyin:
   ```markdown
   ---
   name: skill-adiniz
   description: Skill'in ne yaptığını anlatan tek satırlık açıklama.
   ---

   # Skill Başlığı

   Skill'in ne yaptığını ve hangi CLI aracını kullandığını açıklayın.

   ## Çalıştırılacak komut

   `bash` tool'u ile şunu çalıştır:

       komutunuz --argümanlarla

   ## Sonuç geldikten sonra

   Agent'ın çıktıyı kullanıcıya nasıl sunacağını açıklayın.
   ```
3. Agent'ı yeniden başlatın — skill'iniz katalogda otomatik görünür.

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
