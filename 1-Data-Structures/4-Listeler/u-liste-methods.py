isimler = ['Ada','Yiğit','Hasan','Beril']
yaslar = [1998, 2000, 1998, 1987]

# 1-  "Cenk" ismini listenin sonuna ekleyiniz.
isimler.append("Cenk")
print(isimler)
# 2-  "Sena" değerini listenin başına ekleyiniz.
isimler.insert(0,"Sena")
print(isimler)
# 3-  "Yiğit" ismini listeden siliniz.
#isimler.remove("Yiğit")
isimler.pop(2)
print(isimler)
# 4-  "Yiğit" isminin indeksi nedir ?
i=isimler.index("Sena")
print(i)
# 5-  "Beril" listenin bir elemanı mıdır ?
sonuc = "Beril" in isimler
print(sonuc)
# 6-  Liste elemanlarını ters çevirin.
isimler.reverse()
yaslar=yaslar[::-1]
print(isimler)
print(yaslar)
# 7-  Liste elemanlarını alfabetik olarak sıralayınız.
isimler.sort()
print(isimler)
# 8-  yaslar listesini rakamsal büyüklüğe göre sıralayınız.
yaslar.sort()
print(yaslar)
# 9-  s = "IPhone X,IPhone XR" karakter dizisini listeye çeviriniz.
s = "IPhone X,IPhone XR"
s.split(",")
print(s)
# 10- yaslar dizisinin en büyük ve en küçük elemanı nedir ?
minimumyas=max(yaslar)
print("min",minimumyas)
maximumyas=min(yaslar)
print("max",maximumyas)
# 11- yaslar dizisinde kaç tane 1998 değeri vardır ?
print(yaslar.count(1998))
# 12- yaslar dizisinin tüm elemanlarını siliniz.
yaslar.clear()
print(yaslar)
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
print("3 adet marka giriniz")
markalar=[]
a=input("Marka1 :")
markalar.append(a)
b=input("Marka1 :")
markalar.append(b)
c=input("Marka1 :")
markalar.append(c)
print(markalar)
