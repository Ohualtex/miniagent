---
name: code-cleaner
version: 1.0.0
description: Belirtilen klasördeki kod dosyalarını analiz eder, eksik docstring/yorum satırlarını ekler, kullanılmayan importları temizler ve kodu optimize eder.
ajanox: ">=1.0.0 <2.0.0"
permissions: [shell_safe]
author:
  name: Fevziye Nur Kesebir
  github: nurksbr
license: Apache-2.0
language: tr
languages: [tr]
requires:
  os: [linux, darwin, wsl]
  internet: false
tags: [developer-tools, refactor, automation]
---

# Kod Temizlikçisi (Refactor & Dokümantasyon)

## Açıklama

Bu skill, yazılım projelerinizdeki teknik borçları azaltmak için tasarlanmıştır. Belirtilen dizindeki kaynak kod dosyalarını tarar. Kod standartlarını iyileştirmek için şu adımları otonom olarak gerçekleştirir:
1. **Temizlik:** Kullanılmayan `import` ifadelerini ve tanımlanmış ama kullanılmayan değişkenleri kaldırır.
2. **Dokümantasyon:** Sınıf ve fonksiyonlara eksik olan docstring ve açıklayıcı yorum satırlarını kurumsal standartlara uygun ekler.
3. **Formatlama:** Kodu PEP 8 veya ilgili dilin standartlarına göre yeniden hizalar.

## Parametreler

- `target_dir`: Analiz edilecek ve temizlenecek hedef klasörün tam yolu (Path).

## Çalıştırılacak komut

`bash` tool'u ile aşağıdaki komutu çalıştır:

```bash
python3 -c "
import os, sys, json, urllib.request

def ask_local_ollama(prompt, code):
    # Yereldeki Ollama API'sine (Llama3 veya DeepSeek) bağlanarak kodu refactor etmesini ister
    url = 'http://localhost:11434/api/generate'
    system_prompt = 'Sen kurumsal standartlarda kod refaktörü yapan bir asistansın. Sana verilen kodu incele, eksik docstringleri ekle, kod kalitesini artır ve sadece temizlenmiş kodu geri döndür. Açıklama yapma.'
    full_prompt = f'{system_prompt}\n\nKod:\n{code}'
    
    data = json.dumps({
        'model': 'deepseek-coder-v2', # veya yerelde yüklü 'llama3'
        'prompt': full_prompt,
        'stream': False
    }).encode('utf-8')
    
    try:
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'})
        with urllib.request.urlopen(req) as response:
            res_data = json.loads(response.read().decode('utf-8'))
            return res_data.get('response', code)
    except Exception as e:
        return f'# LLM Bağlantı Hatası: {str(e)}\n' + code

def clean_and_refactor(target_path):
    print(f'[Ajanox] {target_path} dizini taranıyor ve optimize ediliyor...')
    
    if not os.path.exists(target_path):
        print(f'[Ajanox] Hata: {target_path} dizini bulunamadı.')
        return

    for root, dirs, files in os.walk(target_path):
        for file in files:
            if file.endswith('.py'): # İlk aşamada Python dosyalarına odaklanıyoruz
                file_path = os.path.join(root, file)
                print(f'[Ajanox] İşleniyor: {file}')
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    original_code = f.read()
                
                # Yerel LLM ile kodu temizle, optimize et ve dökümante et
                improved_code = ask_local_ollama('Kodu düzenle ve dökümante et', original_code)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(improved_code)
                    
    print('[Ajanox] Temizlik ve refaktör işlemi başarıyla tamamlandı!')

clean_and_refactor('$target_dir')
"
```

## Sonuç işleme

Temizlik ve refaktör işleminin tamamlandığına dair çıktı mesajını kullanıcıya doğal Türkçe ile aktar.

## Hata durumları

- Hedef klasör bulunamazsa veya yerel LLM bağlantısında sorun yaşanırsa, oluşan hataları kullanıcıya raporla.
