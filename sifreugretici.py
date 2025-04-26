import tkinter as tk
from tkinter import messagebox
import random
import string

#sifre üretme
def sifre_uret():
    try:
        uzunluk = int(giris.get())
        if uzunluk <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("hata", "geçerli bir sayı girin.")
        return

    karakterler = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    sonuc_label.config(text="Oluşturulan Şifre: " + sifre)
    kopyalanacak_sifre.set(sifre)

# panoya kopyalama
def panoya_kopyala():
    sifre = kopyalanacak_sifre.get()
    if sifre:
        pencere.clipboard_clear()
        pencere.clipboard_append(sifre)
        messagebox.showinfo("Başarılı", "Şifre panoya kopyalandı.")
    else:
        messagebox.showwarning("Uyarı", "Önce bir şifre üretin.")

# Tkinter ana pencere
pencere = tk.Tk()
pencere.title("Sifre OLuşturucu")
pencere.geometry("400x250")

kopyalanacak_sifre = tk.StringVar()

# arayüz
etiket = tk.Label(pencere, text="Şifre Uzunluğu:", font=("Arial", 12))
etiket.pack(pady=10)

giris = tk.Entry(pencere, font=("Arial", 12), justify="center")
giris.pack()

buton = tk.Button(pencere, text="Şifre Üret", command=sifre_uret, font=("Arial", 12))
buton.pack(pady=10)

sonuc_label = tk.Label(pencere, text="", font=("Arial", 12), fg="blue")
sonuc_label.pack()

kopyala_buton = tk.Button(pencere, text="Panoya Kopyala", command=panoya_kopyala, font=("Arial", 11))
kopyala_buton.pack(pady=10)

pencere.mainloop()
