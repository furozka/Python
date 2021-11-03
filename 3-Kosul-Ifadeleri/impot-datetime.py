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
