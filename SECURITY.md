# Güvenlik Politikası

## ⚠️ Önemli Uyarı

Mini Agent, bir LLM tarafından üretilen **rastgele shell komutlarını** çalıştıran
bir `bash` aracı içerir. Bu doğası gereği tehlikelidir ve **yalnızca eğitim
amaçlıdır**.

**Uygun bir sandbox (Docker, Firecracker, gVisor vb.) olmadan bu agent'ı
production'da ÇALIŞTIRMAYIN.**

---

## Güvenlik Açığı Bildirme

Bir güvenlik açığı keşfederseniz, lütfen herkese açık bir issue **açmayın**.
Bunun yerine:

1. Projeyi yürüten kişiye doğrudan e-posta gönderin (GitHub profiline bakın).
2. Açığı ve tekrarlama adımlarını açıklayın.
3. Kamuya açıklamadan önce düzeltme için makul süre tanıyın.

---

## Bilinen Riskler

- **Kısıtlamasız bash çalıştırma**: LLM herhangi bir komut üretebilir.
- **Girdi temizleme yok**: Kullanıcı girdisi doğrudan modele iletilir.
- **Kimlik doğrulama yok**: Terminale erişimi olan herkes etkileşime geçebilir.
- **Çıktı kesme**: Büyük çıktılar 4000 karakterde kesilir, bu önemli bilgileri
  gizleyebilir.
