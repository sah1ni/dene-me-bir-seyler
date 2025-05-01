def hata_mesaji():
    print("Bir hata kodu girin:")
    print("400 - Hatalı istek")
    print("404 - Sayfa bulunamadı")
    print("500 - Sunucu hatası")
    
    status = int(input("Hata kodunu girin (400, 404, 500): "))
    
    match status:
        case 400:
            print("Hatalı istek!")
        case 404:
            print("Sayfa bulunamadı.")
        case 500:
            print("Sunucu hatası!")
        case _:
            print("Bilinmeyen hata.")

# Fonksiyonu çalıştırmak için:
hata_mesaji()
