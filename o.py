import time

print("Kardeş lokantasına hoşgeldiniz!")

# Yemek Seçimi
secim = input("Lokantamızda 2 çeşit yemek var: Döner ve Pilav. Ne yemek istersiniz? ").lower()

# Yemek Hazırlık Süreci
if secim == "döner":
    print("Döner hazırlanıyor, lütfen bekle...")
    time.sleep(3)
    print("Döner hazır, afiyet olsun!")

elif secim == "pilav":
    print("Pilav hazırlanıyor, lütfen bekle...")
    time.sleep(3)
    print("Pilav hazır, afiyet olsun!")
    
else:
    print("Menümüzde bu yemek yok. Lütfen tekrar deneyin.")
    exit()

# İçecek Seçimi
ic = input("Ne içecek istersiniz? Ayran veya Kola? ").lower()

# İçecek Hazırlık Süreci
if ic == "kola":
    print("Kola hazırlanıyor, lütfen bekle...")
    time.sleep(3)
    print("Kola hazır, afiyet olsun!")

elif ic == "ayran":
    print("Ayran hazırlanıyor, lütfen bekle...")
    time.sleep(3)
    print("Ayran hazır, afiyet olsun!")

else:
    print("Menümüzde bu içecek yok. Lütfen tekrar deneyin.")
    exit()

# Kullanıcıya Teşekkür
print("Afiyet olsun, bizi tercih ettiğiniz için teşekkür ederiz!")
