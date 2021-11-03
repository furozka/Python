isimler = ["Ahmet","ali","Çınar","DeNiz"]
string = "Hello 123456 World."
yillar = [1983, 1999, 2008, 1956, 1986]
dereceler = [20,5,15,-2,0,-6]

# 1- "1-100" arasındaki sayılardan 12' e tam bölünebilen sayı listesi oluşturunuz.
sayilar=[i for i in range(1,100) if i%12==0]
#sayilar=[i if i%12==0 else "not" for i in range(1,100)]
print(sayilar)

# 2- isimler listesindeki her ismi küçük harfe çevirip tersten yazdınız.
sonuc=[i[::-1].lower() for i in isimler]
print(sonuc)

# 3- verilen "string" içindeki rakamları içeren bir liste oluşturunuz.
sonuc=[i for i in string if i.isdigit()]
print(sonuc)
# 4- "yillar" dizisindeki her doğum yılı için yaş bilgisini içeren liste oluşturunuz.
import datetime
today=datetime.datetime.now()
yas=[today.year-i for i in yillar]
print(yas)
# 5- "dereceler" listesinde bulunan hava sıcaklık bilgisine göre eksi değer için buzlanma tehlikesi yazdırınız.
sonuc=[i if i>=0 else "buzlanma tehlikesi" for i in dereceler]
print(sonuc)

"""string=string.split()
print(string)
sonuc=[i for i in string[1]]
print(sonuc)
"""