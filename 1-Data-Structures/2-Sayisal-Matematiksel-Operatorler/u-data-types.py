'''
    Daire Alanı   : πr²
    Daire Çevresi : 2πr    
    ** Yarı çapı verilen bir dairenin alan ve çevresini hesaplayınız. (π: 3.14)

'''
r=float(input("dairein yarı capini giriniz"))
pi = 3.14
print(r**2)
alan=pi*r**2
cevre=2*pi*r
print("alan = ", alan, "\nçevre = ", cevre)

'''
    Bir aracın km cinsinden gittiği yol bilgisini mil olarak yazdırınız.
    mil = km / 1.609344
'''
print("gidilen yolu km cinsinden ngiriniz")
yol=float(input())
mil=yol/1.609344
print(str(yol)+ "km = " +str(mil)+ " mildir.")
