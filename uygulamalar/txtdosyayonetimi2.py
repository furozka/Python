def urun_ekle(ad,fiyat):
    with open("urunler.txt", mode="a", encoding="UTF-8") as f:
        f.write(ad + " "+fiyat+"\n")

urun_ekle("telefon","1000TL")
urun_ekle("bilgisayar","10000TL")
urun_ekle("araba","100000TL")

def kelime_deis(dosya_ismi,eski_kelime, yeni_kelime):
    with open(dosya_ismi, mode="r+", encoding="UTF-8") as f:
        kelimeler=f.read()
        yeni_kelimeler=kelimeler.replace(eski_kelime,yeni_kelime)
        f.seek(0)
        f.write(yeni_kelimeler)
        f.truncate() #cursorun son konumundan itibaren en sona kadar karakterleri siler
        # kelime deişirken daha az karekterli string yazarsan eksik karekterler aşağıda yazılıyo
        # bu karekterleri silmek için truncate kullanıyoruz

kelime_deis("urunler.txt","gramafon","tel")
kelime_deis("urunler.txt","araba","car")