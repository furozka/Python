a, b, c = 2, 5, 12

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile a,b,c toplamının farkı nedir ?
x,y=int(input("2 adet sayi giriniz")),int(input())
sonuc=x*y-(a+b+c)
print(f"{x*y}-{a+b+c}={sonuc}")
# 2- c' nin  b' ye kalansız bölümünü hesaplayınız.
sonuc=(c//b)
print("cnin bye kalansız bölümü",c//b)
# 3- (a,b,c) toplamının mod 3' ü nedir ?
print("mod3: ",(a+b+c)%3)
# 4- b' nin a. kuvvetini hesaplayınız.
print("b**a:",b**a)
# 5- a, *b, c = sayilar işlemine göre c' nin küpü kaçtır ? 
sayilar = 1, 5, 7, 10, 3
a,*b,c=sayilar
print("c küp: ",c**3)
# 6- a, *b, c = sayilar işlemine göre b nin değerleri toplamı kaçtır ?
toplam=sum(b)
print(b)
print(toplam)