"""1 ile 100 arası rasgele sayı üret aşşağı yukarı ile bul
    puanlandırma sistemi
    deneme sayısı
    aşağı yukarı yönlendirme
    hak sayısı
"""
import random

sayi=random.randint(1,100)
print("Sayı tahmin oyununa hoş geldiniz")
hak=int(input("kaç denemede bulacaksınız :"))
bolen=hak
puan=100
count=0
while hak>0:
    tahmin=int(input("Tahmininiz: "))
    if tahmin<sayi:
        print("Yukarı")
        hak-=1
        count+=1
        if hak==0:
            print("Hakkınız bitti Game over sayi: {} idi".format(sayi))
            break
        puan-=(100/bolen)
    elif tahmin>sayi:
        print("Aşağı")
        hak-=1
        count+=1
        if hak==0:
            print("Hakkınız bitti Game over sayi: {} idi".format(sayi))
            break
        puan-=(100/bolen)
    else:
        print("sayiyi bildin sayi: ",sayi)
        print(f"tahminin {tahmin}, {hak} hakkın kala bildin, puanın: {puan} {count} kez denedin. ")
        break

