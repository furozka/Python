import numpy as np
#1-(10,15,30,45,60) numpy dizisi oluştur
np_array=np.array([10,15,30,45,60])

#2- (5-15) arasındaki sayılardan numpy dizisi oluştur
np_array=np.arange(5,15)

#3- (50-100) arasında 5 er 5 er artarak numpy dizisi oluştur
np_array=np.arange(50,100,5)

#4- 10 elemanlı sıfırdan oluşan numpy dizisi
np_array=np.zeros(10)

#5- 10 elemanlı birlerden oluşan numpy dizisi
np_array=np.ones(10)

#6- (0-100) arasında eşit aralıklarla 5 sayıdan oluşan dizi
np_array=np.linspace(0,100,5)

#7- (10-30) arası 5 tane tamsayıdan oluşan dizi
np_array=np.random.randint(10,30,5)

#8-[-1 ile 1] arasında 10 sayıdan oluşan dizi
np_array=np.random.randn(10)

#9- (3x5) boyutlarında (10-50) arasında rasgele bir matris oluşturun
np_array=np.random.randint(10,50,15).reshape(3,5)

#10- Üretilen matrisin satır ve stun toplamlarını hesaplayın
sum_np_array_rows=np_array.sum(axis=1)
sum_np_array_columns=np_array.sum(axis=0)
# print(sum_np_array_rows)
# print(sum_np_array_columns)

#11- Üretilen matrisin en büyük ve en kücük değerlerinin ortalaması
np_array_max=np.max(np_array)
np_array_min=np.min(np_array)
np_array_mean=np.mean(np_array)
# print(np_array_max, np_array_min)

#12- Üretilen matrisin en büyük değerinin indexi
en_buyuk_index=np.argmax(np_array)
# print(en_buyuk_index)

#13- (10-20) arasındaki sayıları içeren arraydan ilk 3 eleman
np_array2=np.arange(10,20)
np_array2_ilkuc=np_array2[:3]
# print(np_array_ilkuc)

#14- Üretilen dizinin elemanlarını tersten yazdırınız
# print(np_array)
# print("-----------------")
# print(np_array[::-1])
# print("-----------------")

#15- Üretilen Matrisin ilk satırını seçiniz
np_array_ilkuc_satir=np_array[:3,:]
# print(np_array_ilkuc_satir)
# print("---------------")

#16- Üretilen matirisn 2. satır 3. stunundaki eleman
np_ikincisatir_ucuncusutun=np_array[1,2]
# print(np_array)
# print(np_ikincisatir_ucuncusutun)
# print("-----------------")

#17- Üretilen matrisin tüm satırlarındaki ilk elemanı seçin
np_tumsatir_ilkeleman=np_array[::,0]
# print(np_array)
# print(np_tumsatir_ilkeleman)

#18- Üretilen matrisin her bir elemanının karesini alınız
np_square=np.square(np_array)
# print(np_array)
# print(np_square)

#19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır?
#aralık -50 ve +50
np_array=np.random.randint(-50,50,15).reshape(3,5)
print(np_array)
print("-------------")
ciftler=np_array[np_array%2==0]
pozitifler=ciftler[ciftler>0]
print(pozitifler)

