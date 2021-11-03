import numpy as np

#np arryı oluşturma
np_array=np.array([1,2,3,4,5,6,7,8,9])

#1 den 9 a kadar array olusturma
result=np.arange(1,10)
print(result)
#1 den 99 a kadar 3 er 3 er artan array oluşturma
result=np.arange(10,100,3)

#10 tane 0 olan array oluşturma
result=np.zeros(10)

#10 tane 1 olan array oluşturma
result=np.ones(10)

#0 ve 100 dahil sayıları 5 eşit parçaya bölme 0 25 50 75 100
result=np.linspace(0,100,5)

#0 ve 5 dahil sayıları 5 eşit parçaya böle 0 1.25 2.5 3.75 5
result=np.linspace(0,5,5)

#0 ile 9 arasında random sayı alma
result=np.random.randint(0,10)

#0 ile 19 arasında random sayı alma
result=np.random.randint(20)

#1 ile 9 arasında 3 sayı alma 
result=np.random.randint(1,10,3)

#0 ile 1 arasında 5 sayı alma
result=np.random.rand(5)

#-1 ile 1 arasında 5 sayı alma
result=np.random.randn(5)

np_array=np.arange(50)
np_multi=np_array.reshape(5,10)
# print(np_multi)
# print(np_multi.sum(axis=1)) #satır toplamı
# print(np_multi.sum(axis=0)) #stun toplamı

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)
result=rnd_numbers.max() #rnd_numbersteki en büyük sayı
result=rnd_numbers.min() #rnd_numbersteki en küçük sayı
result=rnd_numbers.mean() #rnd_numberstaki sayıların mean (ortalama) değeri
result=rnd_numbers.argmax() #rnd_numberstaki en büyük sayının indexi
result=rnd_numbers.argmin() #rnd_numberstaki en küçük sayının indexi
print(result)