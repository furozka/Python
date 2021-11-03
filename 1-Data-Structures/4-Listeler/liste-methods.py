sayilar=[1,5,8,3,9,7,47]
harfler=['a','b','e','s','a','y']
sonuc = min(sayilar) #sayilarda min max
print("Min",sonuc)
sonuc = max(sayilar)
print("Max",sonuc)
sonuc=min(harfler)
print("min Harf",sonuc) #harflerde min max
sonuc=max(harfler)
print("Max Harf",sonuc) 
#ekleme işlemleri
sayilar.append(10) #listenin sonuna 10 sayisini ekler
sonuc=sayilar
print(sonuc)
sayilar.insert(4,5) #4 numaralı indise 5 sayısını ekler
sonuc=sayilar
print(sonuc)
#silme işlemleri
sayilar.pop() #listenin sonundaki elemanı siler
sonuc=sayilar
print(sonuc)
sayilar.pop(1) #1. indisteki sayiyi siler
sonuc=sayilar
print(sonuc)
sayilar.remove(47) #47 değerini listeden siler silmek istediğin değeri yazıyosun
sonuc=sayilar
print(sonuc)
harfler.remove("a") #harfler=['a','b','e','s','a','y'] baştaki a değerrini siler diğğer a yı silmek için tekrar
sonuc=harfler
print(sonuc)
#sıralama işlemleri
sayilar.sort() #küçükten büyüğe sıralar
sonuc=sayilar
print(sonuc)
harfler.sort()#a dan z ye sıralar ilk harflere göre ve sonra ikinci harfler
sonuc=harfler
print(sonuc) 
sayilar.reverse() # büyükten küçüğe sıralar 
sonuc=sayilar
print(sonuc)
harfler.reverse() # z den a ya sıralar
print(harfler)
sonuc=sayilar.count(5) #kaç tane 5 sayısı olduğuna bakar bir değişkene atamalısın tutmak için
print(sonuc)
sonuc=sayilar.index(3) #3 sayisi hangi indexte olduğunu gösterir
print(sonuc)
sayilar.clear() #listenin tüm elemanlarını siler boş liste kalır
print(sayilar)
