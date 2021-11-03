#bankamatik Uygulaması
#Ekstra yapılabilecekler
######Para yatır fonksiyonu
######İlk ek hesabı doldur
######Ek hesaptan çekilen parayı tarihini alıp günlük faiz üzerinden hesaplayıp para yatırırken bakiyeden düşme

def hesapOlustur(**kwargs):
    ad=input("isminiz: ")
    hesapno=input("hesap numaranız: ")
    bakiye=float(input("bakiyeniz:"))
    ekhesap=float(input("ek hesap bakiyeniz: "))
    yeniHesap={
        "ad": ad,
        "hesap no": hesapno,
        "bakiye": bakiye,
        "ekhesap": ekhesap
    }
    return yeniHesap
FurkanHesap={
    "ad": "Furkan ÖZKAN",
    "hesap no": "123456",
    "bakiye": 5000,
    "ekhesap": 2000
}
IbrahimHesap={
    "ad": "İbrahim ÖZKAN",
    "hesap no": "124578",
    "bakiye": 3000,
    "ekhesap": 1000
}

def paraCekme(hesapAdi):
    print(hesapAdi)
    cekilecek=float(input("Çekmek istediğiniz para miktarı: "))
    if cekilecek>hesapAdi["bakiye"]:
        print(f"hesabınızdaki bakiye {hesapAdi['bakiye']} kadar ve yeterli değil ek hesaptan para çekmek istermisiniz")
        cevap=input("press y or n")
        if cevap=="y":
            if cekilecek>hesapAdi["bakiye"]+hesapAdi["ekhesap"]:
                print(f"ek hesap dahil toplam {hesapAdi['bakiye']+hesapAdi['ekhesap']} TL çekebilirsiniz yeterli bakiye yok")
            else:
                hesapAdi['ekhesap']=hesapAdi['ekhesap']-(cekilecek-hesapAdi['bakiye'])
                hesapAdi['bakiye']=0
                print(f"{cekilecek} TL para çektiniz hesabınızda: {hesapAdi['bakiye']} TL kaldı ve ek hesabınızda: {hesapAdi['ekhesap']} TL kaldı")
        else:
            print("İşlem sonlandı")
    elif cekilecek<hesapAdi["bakiye"]:
        hesapAdi["bakiye"]=hesapAdi["bakiye"]-cekilecek
        print(f"{cekilecek} TL para çektiniz hesabınızda {hesapAdi['bakiye']} TL kaldı")
    hesapSorgu(hesapAdi)
def hesapSorgu(hesapAdi):
    print(f"Hesabinizde {hesapAdi['bakiye']} TL bakiye ve ek hesabinizda {hesapAdi['ekhesap']} TL bulunmaktadır")
paraCekme(FurkanHesap)

print("*************************")
paraCekme(IbrahimHesap)


