# 1- Girilen 2 sayıdan hangisi büyüktür ?
x=int(input("birinci sayi: "))
y=int(input("ikinci sayi: "))
if x>y:
    print(f"{x}>{y}")
elif x<y:
    print(f"{y}>{x}")
else:
    print(f"{x}={y}")
# 2- Girilen bir sayının tek mi çift mi olduğunu yazdırın.
x=int(input("tek veya çift sayi giriniz"))
if x%2==0:
    print(f"{x} is even")
else:
    print(f"{x} is odd")
# 3- Girilen bir sayının negatif pozitif durumunu yazdırın.
x=int(input("pozitif veya negatif sayi giriniz"))
if x<0:
    print(f"{x} is negative")
elif x>0:
    print(f"{x} is positive")
else:
    print(f"{x} is 0 notr")
# 4- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız.
vize=int(input("vize notunuz: "))
final=int(input("final notunu: "))
print(f"Ortalamanız: {(vize*40/100)+(final*60/100)}")
# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
email="furozka05@gmail.com"
parola="111111"
x=input("E-mail adresinizi giriniz")
y=input("şifrenizi giriniz")
print(f"e mail hesabını {x==email} girdiniz Şifrenizi {y==parola} girdiniz")
