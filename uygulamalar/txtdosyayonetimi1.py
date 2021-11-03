def dosya_kopyala(dosya_ismi, yeni_dosya_ismi):
    with open(dosya_ismi,"r",encoding="UTF-8") as f1:
        icerik=f1.read()
    with open(yeni_dosya_ismi,"w",encoding="UTF-8") as f2:
        f2.write(icerik)

dosya_kopyala("markalar.txt","kopya_markalar.txt")
def ters_cevir(dosya_ismi, yeni_dosya_ismi):
    with open(dosya_ismi,"r",encoding="UTF-8") as f1:
        icerik=f1.read()
    with open(yeni_dosya_ismi,"w",encoding="UTF-8") as f2:
        f2.write(icerik[::-1])
            

ters_cevir("markalar.txt","ters_markalar.txt")

def bilgilendir(dosya_ismi):
    with open(dosya_ismi,"r",encoding="UTF-8") as f:
        satir_sayisi=len(f.readlines())
        f.seek(0)
        kelime_sayisi=len(f.read().split())
        f.seek(0)
        karekter_sayisi=sum([len(i) for i in f.readlines()])
        return f"Satır sayısı: {satir_sayisi} Kelime sayisi: {kelime_sayisi} Karekter sayisi: {karekter_sayisi}"

print(bilgilendir("markalar.txt"))



