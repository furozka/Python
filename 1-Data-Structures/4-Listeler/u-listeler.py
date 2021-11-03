# 1-  "Samsung S5,Samsung S6,Samsung S7,Samsung S8" elemanlarına sahip bir liste oluşturunuz.
telefonlar= ["Samsung S5","Samsung S6","Samsung S7","Samsung S8"]
# 2-  Liste Kaç elemanlıdır ?
print(len(telefonlar))
# 3-  Listenin ilk ve son elemanı nedir ?
print(telefonlar[0],telefonlar[-1])
# 4-  "Samsung S5" değerini "Samsung S9" ile değiştirin.
telefonlar[0]="Samsung S9"
print(telefonlar)
# 5-  "Samsung S6" listenin bir elemanı mıdır ?
if "Samsung S6" in telefonlar:
    print("Samsung S6 is in telefonlar")
else:
    print("no S6 is not in telefonlar")
# 6-  Listenin -3 indeksindeki değer nedir ?
print(telefonlar[-3])
# 7-  Listenin ilk 2 elemanını alın.
print(telefonlar[:2])
# 8-  Listenin son 2 elemanı yerine "Samsung S9" ve "Samsung S10" değerlerini ekleyin.
telefonlar[-2:]="Samsung S9","Samsung S10"
print(telefonlar)
# 9-  Listenin üzerine "IPhone X" ve "IPhone XR" değerlerini ekleyin.
telefonlar=telefonlar + ["IPhone X","IPhone XR"]
print(telefonlar)
# 10- Listenin son elemanını silin.
del telefonlar[-1]
print(telefonlar)
# 11- Liste elemanlarını tersten yazdırınız.
print(telefonlar[::-1])
# 12- Aşağıdaki verileri bir liste içinde saklayınız. 

      # kullaniciA: Yiğit Bilgi 2010, (70,60,70)
      # kullaniciB: Sena Turan  1999, (80,80,70)
      # kullaniciC: Ahmet Turan 1998, (80,70,90) 
kullaniciA=["Yiğit","Bilgi","2010","(70,60,70)"]
kullaniciB=["Sena","Turan","1999","(80,80,70)"]
kullaniciC=["Ahmet","Turan","1998","(80,70,90)"]
ogrenciler=[kullaniciA,kullaniciB,kullaniciC]
print(ogrenciler)