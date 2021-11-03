# 1- 3 ürün bilgisini (id,ad,fiyat) kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.
# 2- Ürün id bilgisini kullanıcıdan alıp ilgili ürün bilgisini gösterin.
urunler={}
for i in range(1,4):
    id=input("id: ")
    ad=input("ürün adı :" )
    fiyat=input("fiyatı: ")
    urunler[id]={
        "ad": ad,
        "fiyat": fiyat
    }
istenen=(input("ürün ID'sini giriniz: "))
print(urunler[istenen])

"""
urundict={1:{ad1: int(fiyat1)},2:{ad2:int(fiyat2)},3:{ad3:int(fiyat3)}}
print(urundict)

"""