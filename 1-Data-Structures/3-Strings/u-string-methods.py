website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."
# 1- ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
a=' Hello World '
print(a)
result=a.strip()
print(result)
result=a.lstrip()
print(result)
result=a.rstrip()
print(result)
result=a.lstrip(" Helo")
print(result)
yazi="abcdead"
result=yazi.strip("a")
print(result)
# 2- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
a='www.sadikturan.com'
result=a.strip("w.moc")
print(result)
# 3- 'kursAdi' karakter dizisinin tüm karakterlerini küçük harf yapın.
result=kursAdi.lower()
print(result)
# 4- 'website' içinde kaç tane a karakteri vardır ? (count('a'))
result=website.count("a")
print(result)
# 5- 'website' "www" ile başlayıp com ile bitiyor mu?
result=website.startswith("www")
print(result)
result=website.endswith("com")
print(result)
# 6- 'website' içinde '.com' ifadesi var mı?
result=website.find(".com")
print(result)
# 7- 'kursAdi' içindeki karakterlerin hepsi alfabetik mi? (isalpha, isdigit)
result=kursAdi.isalpha()
print(result)
result=kursAdi.isdigit()
print(result)
# 8- 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
sonuc = 'Contents'.ljust(50,'*')
sonuc = 'Contents'.rjust(50,'*')
result="Contents".center(50,"*")
print(result)
# 9- 'kursAdi' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result=kursAdi.replace(" ","-")
print(result)
# 10-'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
result="Hello World".replace("World","There")
print(result)
# 11-'kursAdi' karakter dizisini boşluk karakterlerinden ayırın.
result=kursAdi.split()
print(result)