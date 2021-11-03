def not_hesapla(satir):
    notlar=satir.split(":")
    ogrenci_adi=notlar[0]
    notlar=notlar[1].split(",")
    ortalama=round((sum([int(i) for i in notlar])/3),2)
    if ortalama>=90:
        harf="AA"
    elif 80<=ortalama<90:
        harf="AB"
    elif 70<=ortalama<80:
        harf="BB"
    elif 60<=ortalama<70:
        harf="CC"
    elif 50<=ortalama<60:
        harf="DD"
    elif ortalama<50:
        harf="FF"
    
    
    return f"{ogrenci_adi}: {harf}"

def ortalamaları_oku():
    with open("sinav_notlari.txt",mode="r",encoding="UTF-8") as f:
        for i in f:
            print(not_hesapla(i))
def not_gir():
    ad = input("Öğrenci adı: ")
    soyad = input("Öğrenci soyadı: ")
    not1 = int(input("Öğrenci not1: "))
    not2 = int(input("Öğrenci not2: "))
    not3 = int(input("Öğrenci not3: "))

    with open("sinav_notlari.txt",mode="a",encoding="UTF-8") as f:
        f.write(f"{ad} {soyad}:{not1},{not2},{not3}\n")
def not_kayitet():
    with open("sinav_notlari.txt",mode="r",encoding="UTF-8") as f:
        liste=[]
        for i in f:
            liste.append(not_hesapla(i))
        with open("sonuclar.txt",mode="w", encoding="UTF-8") as f2:
            for i in liste:
                f2.write(i+"\n")

while True:
    islem = input("1-Notları Oku\n2-Not Gir\n3-Notları Kayıt Et\n4-Çıkış\n")

    if islem=="1":
        ortalamaları_oku()
    elif islem=="2":
        not_gir()
    elif islem=="3":
        not_kayitet()
    else:
        break
