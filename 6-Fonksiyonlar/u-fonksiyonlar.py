# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 
def metinyaz(kelime,num):
    print(kelime*num)
metinyaz("pokemon\n",5)
# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.
def dikdortgen(kisa,uzun):
    alan=kisa*uzun
    çevre=2*(kisa+uzun)
    print(f"alan: {alan} ve çevre: {çevre}")
dikdortgen(7,15)

# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)
def yaziTura():
    import random
    sayi=random.randint(1,2)
    if sayi==1:
        print("yazi")
    elif sayi==2:
        print("tura")
yaziTura()
# 3- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.
def asalSayiFinder(x,y):
    asallar=[]
    for i in range(x,y):
        if i==2:
            asallar.append(2)
        else:
            for j in range(2,i):
                if i%j==0:
                    break
                elif i==j+1:
                    asallar.append(i)
    return asallar
print(asalSayiFinder(1,100))
# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.
def bolenler(x):
    bolenler=[1]
    i=2
    while i<x:
        if x%i==0:
            bolenler.append(i)
            x=x/i
        else:
            i+=1
    return bolenler

print(bolenler(27))
