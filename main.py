from unidecode import unidecode
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pyperclip
from tkinter import messagebox
import subprocess

subprocess.call(["afplay", "/Users/neaderlord/Documents/Belgeler - Berkay MacBook Air/Belgeler/Türkçe İngilizce Harf Çevirici/music/yt1s.com - Breaking Bad Theme Low Quality-[AudioTrimmer.com].mp3"])

#Ekran Oluşturma
ekran = tk.Tk()

#Ekran İsmi
ekran.title("Türkçe - İngilizce Karakter Değiştirici")

#Ekran Boyutu
ekran.geometry("800x500")

#Çeviri Butonu İşlevi
def çeviri():
    trgirdi = trentry.get("1.0", tk.END)
    çevtxt = unidecode(trgirdi)
    outlbl.config(text=çevtxt)

#Kopyala Butonu İşlevi
def kopyala():
    kopy = outlbl.cget("text")
    pyperclip.copy(kopy)
    if kopy == "":
        messagebox.showerror(title="Hata!", message="Lütfen Çeviri Yapın")
    else:
        messagebox.showinfo(title="Başarılı!", message="Başarılı Şekilde Kopyalandı")
    
#Uygulama Label
uyglbl = Label(ekran, text="Türkçe - İngilizce", font=("Ariel", "24"))
uyglbl.pack(pady=10)

#Türkçe Entrysi
trentry = Text(ekran, width=50, height=10)
trentry.pack() 

#Output Kutusu
left = LabelFrame(ekran, text="Output...", width=350, height=150, bg="Grey")
left.pack(pady=5)

#Output Yazısı
outlbl = Label(left, text="", width=38, height=8)
outlbl.pack()

#Çevir Butonu
çevir = Button(ekran, text="Çevir", font=("Ariel", "15"), bg="Grey", width=6, command=çeviri)
çevir.place(x=450, y=360)

#Kopyala Butonu
kopya = Button(ekran, text="Kopyala", font=("Ariel", "15"), bg="Grey", command=kopyala)
kopya.place(x=255, y=360)

mainloop()

