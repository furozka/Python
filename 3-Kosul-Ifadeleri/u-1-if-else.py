# 1- Girilen bir sayının 50-100 arasında olup olmadığını kontrol ediniz.
sayi=int(input("sayigirin: "))
if 50<sayi<100:
    print("sayi 50 ile 100 arasındadır")
else:
    print("sayi 50 ile 100 arasında değildir.")
#2- Girilen bir sayının pozitif tek sayı olup olmadığını kontrol ediniz.
sayi=int(input("sayi giriniz: "))
if sayi>0:
    if sayi%2!=0:
        print("sayi pozitif tekdir.")
    else:
        print("sayi pozitiftir çifttir")
elif sayi%2!=0:
    print("sayi pozitif değildir tekdir.")
else:
    print("sayi pozitif değildir çifttir.")
#3- Username ve parola bilgileri ile giriş kontrolü yapınız. 
_username = "sadikturan"
_password = "1234"
un=input("username: ")
pw=input("pasword: ")
if un==_username:
    if pw==_password:
        print("Basarıyla girdiniz")
    else:
        print("şifre hatalı")
elif un!=_username and pw==_password:
    print("username hatalı.") 
else:
    print("Şifrede usernamede hatalı")
# 4- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.
a=int(input("sayi1: "))
b=int(input("sayi2: "))
c=int(input("sayi3: "))
if a>b and a>c:
    print(f"{a} en büyük")
elif b>a and b>c:
    print(f"{b} en büyük")
elif c>a and c>b:
    print(f"{c} en büyük")
# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
#    a-) Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
#    b-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
#    c-) Finalden 70 alındığında ortalamanın önemi olmasın.
vize1=int(input("vize1: "))
vize2=int(input("vize2: "))
final=int(input("final: "))
ortalama=((vize1+vize2)/2*60/100)+(final*40/100)
print(f"ortalama: {ortalama}")
if ortalama>=50 and 70>final>=50:
    print(f"ortalama: {ortalama}>=50 ve final: {final}>=50 olduğu için geçtiniz")
elif final>=70 and ortalama<50:
    print(f"ortalamanız : {ortalama}<50 olmasına rağmen final notunuz: {final}>=70 olduğundan geçtiniz")
else:
    print("kaldınız")
# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#    Formül: (Kilo / boy uzunluğunun karesi)
#    Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#    0-18.4    => Zayıf 
#    18.5-24.9 => Normal  
#    25.0-29.9 => Fazla Kilolu
#    30.0-34.9 => Şişman (Obez)
ad=input("adınız: ")
kilo= float(input("kilonuz: "))
boy= float(input("boyunuz: "))
if boy>=100:
    boy=boy/100
sonuc=round(kilo/(boy**2),2)
if sonuc<=18.4:
    print(f"zayifsiniz indexiniz: {sonuc}")
elif 18.5<=sonuc<=24.9:
    print(f"normalsiniz indexiniz: {sonuc}")
elif 25.0<=sonuc<=29.9:
    print(f"fazla kilolusunuz indexiniz: {sonuc}")
elif 30.0<=sonuc<=34.9:
    print(f"şişman(obez)siniz indexiniz: {sonuc}")
else:
    print("ayvayı yediniz")

