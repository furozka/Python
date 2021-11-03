# 1- Çarpım tablosu hazırlayınız.
for i in range(1,11):
    print('*************')
    for k in range(1,11):
        print(f"{i}x{k}={i*k}")
# 2- Girilen bir sayının asal olup olmadığını kontrol ediniz..
#    Asal Sayı 1 ve kendisi hariç tam böleni olmayan sayılara denir.
sayi=int(input("Sayi Girin: "))
asal=True
for i in range(2,sayi):
    if sayi%i==0:
        asal=False
        break
if asal:
    print("asaldır")
else:
    print("değildir")
            
    