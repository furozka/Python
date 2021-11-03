website = "http://www.sadikturan.com"
kursAdi = "Python Dersleri: Sıfırdan İleri Seviye Python Programlama."

# 1- 'kursAdi' karakter dizisinde kaç karakter bulunmaktadır ?
result=len(kursAdi)
print(f"1. soru\n{result}")
result=len(website)
# 2- 'website' içinden www karakterlerini alın.
result=website[7:10]
print(f"2. soru\n{result}")
# 3- 'website' içinden com karakterlerini alın.
karekterSayisi=len(website)
result=website[karekterSayisi-3:karekterSayisi]
print(f"3. soru\n{result}")
# 4- 'kursAdi' içinden ilk 15 ve son 15 karakterlerini alın.
karekterSayisi=len(kursAdi)
result=website[:16]+website[-1:-16:-1]
print(f"4. soru\n{result}")
# 5- 'kursAdi' ifadesindeki karakterleri tersten yazdırın.
result=kursAdi[::-1]
print(f"5. soru\n{result}")
# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
result="Hello world"
result=result[:6]+"W"+result[7::]
print(f"7. soru\n{result}")
# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
result="abc" #print(result*3)
print(f"8. soru\n{result*3}")

# 9- Aşağıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
name, surname, age, job = 'Sadık','Turan', 37, 'öğretmen' 
#    'Benim adım Sadık Turan, Yaşım 37 ve mesleğim öğretmen.' 
print(f"Benim adım {name} {surname}, Yaşım {age} ve mesleğim {job}")