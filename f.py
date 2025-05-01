baslangic = int(input("Başlangıç sayısını girin: "))
bitis = int(input("Bitiş sayısını girin: "))

for n in range(baslangic, bitis + 1):
    if n < 2:
        continue  # 2'den küçük sayılar asal olamaz
    for x in range(2, n):
        if n % x == 0:
            print(f"{n} asal değil, çünkü {n} = {x} * {n//x}")
            break
    else:
        print(f"{n} asal bir sayıdır")

