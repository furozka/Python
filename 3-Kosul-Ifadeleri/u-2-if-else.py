# Bir aracın yakıt tipine göre (benzin,dizel) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu
# hesaplayan uygulamayı yapınız.

###### YAKIT TÜKETİM MALİYETİ #######
benzinFiyat = 6.69
dizelFiyat = 5.86
toplamYakitUcreti = 0

while True:
    tip=input("aracın tipi: dizel yada benzin ")
    if tip=="dizel":
        yol=int(input("gidilen yol: km cinsinden "))
        toplamYakitUcreti=yol*dizelFiyat
        print(f"Toplam yakıt maliyeti: {toplamYakitUcreti}TL")
        break
    elif tip=="benzin":
        yol=int(input("gidilen yol: km cinsinden "))
        toplamYakitUcreti=yol*benzinFiyat
        print(f"Toplam yakıt maliyeti: {toplamYakitUcreti}TL")
        break
    else:
        print("\ndizel yada benzini seçiniz\n ")
        pass
