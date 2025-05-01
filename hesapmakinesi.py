print("Hesap makinesine hoşgeldiniz. Umarım iyisinizdir!")
ilk = int(input("Lütfen işlem yapmak istediğiniz birinci sayıyı girin: "))
son = int(input("LÜtfen işlem yapmak istediğiniz ikinci sayıyı girin: "))
islem = input("Yapmak istediğiniz işlemi seçin: +, -, *, / : ") #soru işaretinin sağında boşluk olması gerek.

if islem == "+":
	sonuc = ilk + son
	print(f"Sonuç budur abi: {ilk} + {son} = {sonuc}")
elif islem == "-":
	sonuc = ilk - son
	print(f"Sonuç budur abi: {ilk} - {son} = {sonuc}")
elif islem == "*":
	sonuc = ilk * son
	print(f"Sonuc budur abi: {ilk} * {son} = {sonuc}")
elif islem == "/":
	if son != 0:
		sonuc = ilk / son
		print(f"Sonuc: {ilk} / {son} = {sonuc}")
	else:
		print("sıfıra bölünemez lütfen ikinci sayıyı değiştirin.")
else:
	print("geçersiz bir işlem türü girdiniz lütfen seçeneklerden birini seçiniz.")						
