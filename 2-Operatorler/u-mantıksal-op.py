# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
sayi=int(input("50-100 arasi sayi giriniz: "))
if 50<sayi<100:
    print("sayi 50 ve 100 arasındadir.")
else:
    print("sayi 50 ile yüz arasında değildir")
# 2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.
sayi=int(input("pozitif tek sayi giriniz: "))
if sayi>0 and sayi%2!=0:
    print(f"{sayi} pozitif tek sayidir")
else:
    print(f"{sayi} pzitif tek sayi değildir")
# 3- Username ve parola bilgileri ile giriş kontrolü yapınız. 
username="furozka05"
parola="111111"
x=input("username: ")
y=input("parola: ")
if x==username and y==parola:
    print("Başarıyla giriş yaptınız")
else:
    print("username yada parola hatalı")
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a=int(input("Sayi1: "))
b=int(input("Sayi2: "))
c=int(input("Sayi3: "))
if a>b and a>c:
    print(f"{a} en büyüktür")
elif b>a and b>c:
    print(f"{b} en büyüktür")
elif c>a and c>b:
    print(f"{c} en büyüktür")
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    b-) Finalden 70 alındığında ortalamanın önemi olmasın.
vize1=int(input("vize1: "))
vize2=int(input("vize2: "))
final=int(input("final: "))
ortalama=((vize1+vize2)/2*60/100)+(final*40/100)
if (ortalama>50 and final>50) or final>70:
    print(f"ortalamanız {ortalama} ve geçtiniz!")
else:
    print("kaldınız")
# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)
ad=input("Name: ")
kilo=float(input("Kilo: "))
boy=float(input("Boy: "))
deger=round((kilo/boy/boy),2)
if deger<=18.4:
    print(f"{ad} kilo indeksiniz {deger} ve Zayıfsınız")
elif 18.5<=deger<=24.9:
    print(f"{ad} kilo indeksiniz {deger} ve Normalsiniz")
elif 25.0<=deger<=29.9:
    print(f"{ad} kilo indeksiniz {deger} ve Fazla Kilolusunuz")
else:
    print(f"{ad} kilo indeksiniz {deger} ve Şişman (obez)")



