# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz. 
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır. 
name=input("isminizi girin: ")
age=int(input("Yasınızı girin: "))
egitim=input("Egitim durumuzu girin ilkokul-ortaokul-lise-universite: ")
if (age>=18 and egitim=="lise") or (age>=18 and egitim=="universite"):
    print("Ehliyet alabilirsiniz")
elif age<18:
    print("Yasınız 18den kucuk oldugundan ehliyet alamazsınız")
elif egitim=="ilkokul" or egitim=="ortaokul":
    print("Egitim durumunuz nedeniyle ehliyet alamazsınız")
# 2- Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre not aralığına karşılık 
# gelen not bilgisini yazdırınız.
#    0 -24  => 0
#    25-44  => 1
#    45-54  => 2
#    55-69  => 3
#    70-84  => 4
#    85-100 => 5
yazili1=int(input("birinci yazili sonucunuz: "))
yazili2=int(input("ikinci yazili sonucunuz: "))
sozlu=int(input("sozlu notunuz: "))
ortalama=int((yazili1+yazili2+sozlu)/3)
if 0<=ortalama<=24:
    print("karne notunuz: 0 ortalamanız: ",ortalama)
elif 25<=ortalama<=44:
    print("karne notunuz: 1 ortalamanız: ",ortalama)
elif 45<=ortalama<=54:
    print("karne notunuz: 2 ortalamanız: ",ortalama)
elif 55<=ortalama<=69:
    print("karne notunuz: 3 ortalamanız: ",ortalama)
elif 70<=ortalama<=84:
    print("karne notunuz: 4 ortalamanız: ",ortalama)
elif 85<=ortalama<=100:
    print("karne notunuz: 5 ortalamanız: ",ortalama)
# 3- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
#    1. Bakım => 1. yıl     
#    2. Bakım => 2. yıl      
#    3. Bakım => 3. yıl     
#    ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız..
#    *** datetime modülünü kullanmanız gerekiyor.  
#    (simdi) - (2018/8/1) => gün
import datetime
tarih=input("trafige cikis tarihini giriniz (2019/08/15): ")
tarih=tarih.split("/")
simdi= datetime.datetime.now()
print(simdi)
cikis = datetime.datetime(int(tarih[0]),int(tarih[1]),int(tarih[2]))
print(cikis)
fark=simdi-cikis
print(fark)
gun=fark.days
print(gun)
if gun<=365:
    print("birinci servis bakımı")
elif 365<gun<=730:
    print("ikinci servis bakımı")
elif 730<gun<=1095:
    print("üçüncü servis bakımı")


