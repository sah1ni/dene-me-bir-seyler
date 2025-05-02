import time

print("Kardeş lokantasına hoşgeldiniz ne yemek istersiniz?")
secim = input("Döner, Pilav, Makarna vardır sadece, ne yemek isterseniz? ").lower()

if secim == "pilav":
	print("pilavınız hazırlanıyor lütfen bekleyin.")
time.sleep(5)
print("pilavınız hazırdır abi afiyet olsun.")

bsk = input("başka bir şey istermisiniz? (evet / hayır) ").lower() 
if bsk == "evet":
	print("başka bir eleman bakıcak abi biraz bekle lütfen.")
if bsk == "hayır":
	print("o zaman afiyet olsun abi.")

elif secim == "döner":
	print("peki hangi tür istersin abi? ")	
tr = input("dürüm, tombik, ekmek arasımı olsun abi? ").lower()

if tr == "dürüm":
	print("hazırlanıyor abi 2dk sürecek sanırım.")
time.sleep(3)
print("dürüm hazır abi afiyet olsun.")

elif tr == "tombik":
	print("hazırlanıyor abi 2dk sürecek sanırım.")	
time.sleep(3)
print("tombik hazır abi afiyet olsun.")

elif tr == "ekmek arası":
	print("hazırlanıyor 2 dakika bekleyin")
time.sleep(3)
print("yarım ekmek hazır abi afiyet olsun.")
else:
	print("ondan yok abi kusura kalma")
	


	
