---
name: file-create
version: 0.1.0
description: Yeni bir dosya oluşturur; uzantıya göre uygun boilerplate template uygular.
icon: "📝"
example_prompt: "~/Desktop/script.py adlı boş Python dosyası oluştur"
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe, file_write]
license: MIT
language: tr
languages: [tr, en]
requires:
  binaries: [python3]
  internet: false
tags: [file, create, scaffold, dev]
---

# File Create Skill

Belirtilen yolda yeni bir dosya oluşturur. Uzantı tanınıyorsa o dil için
küçük bir boilerplate template uygular. **Asla mevcut dosyanın üzerine
yazma** — varsa kullanıcıdan onay iste.

## Çalıştırılacak komut

**1. Mevcudiyet kontrolü (önce):**

```
test -e <yol> && echo EXISTS || echo OK
```

`EXISTS` dönerse kullanıcıya sor: "Dosya zaten var, üzerine yazılsın mı?"
Onay yoksa dur.

**2. Boş dosya oluşturma:**

```
touch <yol>
```

**3. Template ile dosya oluşturma (uzantıya göre):**

Aşağıdaki template'lerden uygun olanı seç, sonra Python ile yaz:

```
python3 -c "open('<yol>','w').write('<template>')"
```

**Template'ler:**
- `.py`   → `#!/usr/bin/env python3\n\n`
- `.sh`   → `#!/usr/bin/env bash\nset -euo pipefail\n\n`
- `.html` → tam HTML5 boilerplate (doctype + meta + title + body)
- `.json` → `{}\n`
- `.md`   → `# Başlık\n\n`
- `.java` → `public class <CLASSNAME> {\n    public static void main(String[] args) {\n        \n    }\n}\n` (CLASSNAME dosya adından, uzantısız)
- Tanınmayan uzantı → boş dosya (`touch`)

**4. Script tipleri için çalıştırma izni:**

```
chmod +x <yol>
```

Sadece `.py` ve `.sh` için.

## Sonuç işleme

Kullanıcıya:
- Oluşturulan dosyanın tam yolunu söyle
- Hangi template'in uygulandığını belirt (örn. "Python shebang eklendi")
- `.java` için class adının dosya adından üretildiğini belirt

## Hata durumları

- **Dosya zaten var:** Onay olmadan üzerine yazma.
- **Dizin yok:** Önce `mkdir -p <dizin>` öner ya da onaylı ise çalıştır.
- **Yazma izni yok:** Hedef dizine yazma izninin olmadığını bildir.
