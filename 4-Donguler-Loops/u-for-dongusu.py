sayilar = [1,5,16,35,57,72,75,10]
# 1- sayilar listesindeki her bir elemanı yazdırın.
for i in sayilar:
    print(i)
# 2- Sayilar listesindeki hangi sayılar 5'in katıdır ?
for i in sayilar:
    if i%5==0:
        print("5in katı olan sayilar:",i)
# 3- Sayilar listesinde sayıların toplamı kaçtır ?
summ=0
for i in sayilar:
    summ=summ+i
print("Toplam: ",summ)
summ=sum(sayilar)
print("sum methodu ile toplam: ",summ)
# 4- Sayilar listesindeki çift sayıların karesini alınız.
for i in sayilar:
    if i%2==0:
        print("çift sayi karesi: ",i**2)
# 5- urunler listesindeki tüm ürünlerin 2.karakterlerini ekrana yazdırın.
urunler = ['iphone 8','iphone 7','iphone X','iphone XR','samsung S10']
for i in urunler:
    print("liste elemanı ikinci karekteri",i[1])
# 6- urunler listesinde içinde 'iphone' geçen kaç ürün vardır? (index,find)
count=0
for i in urunler:
    if i.find("iphone")>-1:
        count+=1
print(count)
