#    Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içinde saklayınız.
#    ** ürün sayısını kullanıcıya sorun.
#    ** dictionary listesi yapısı (urunAdi, fiyat) şeklinde olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin.
adet=int(input("kac ürün girmek istiyorsunuz: "))
i=1
urunler=[]
while i<=adet:
    urunAdi=input("Urunun adı: ")
    fiyat=input("fiyat: ")
    urunler.append(
        {
            "urun adı": urunAdi,
            "fiyat": fiyat
        }        
    )
    i+=1
for i in urunler:
    print(i)