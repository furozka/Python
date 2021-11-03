sayilar = [4,6,9,10,35,57,89,125,244]

# 1: sayilar listesini while ile ekrana yazdırın.
i=0
while i<len(sayilar):
    print(sayilar[i])
    i+=1
while sayilar:
    print(sayilar.pop(0))
print(sayilar)
# 2: Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları 
# ekrana yazdırın.
baslangıc=int(input("baslangic degeri: "))
bitis=int(input("bitis degeri: "))
i=baslangıc
while i<bitis:
    if i%2!=0:
        print(i)
    i+=1
# 3: 1-100 arasındaki sayıları azalan şekilde yazdırın.
i=100
while i>=1:
    print(i)
    i-=1
# 4: Kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın.
sayilar=[]
i=1
while i<=5:
    sayi=int(input(f"sayi{i}'i giriniz: "))
    sayilar.append(sayi)
    i+=1
sayilar.sort()
print(sayilar)