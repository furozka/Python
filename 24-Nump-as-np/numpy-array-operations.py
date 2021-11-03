import numpy as np

numbers1=np.random.randint(10,100,6)
numbers2=np.random.randint(10,100,6)
print(numbers1)
print(numbers2)
print("----------------------------")
result=numbers1+numbers2 #iki dizinin aynı indexteki elemanlarını toplar

result=numbers2+10
result=numbers1-numbers2
result=numbers1*numbers2
result=numbers2*10
result=numbers1/numbers2
result=numbers2/10
result=np.sin(numbers2)
result=np.cos(numbers2)
result=np.sqrt(numbers2)
result=np.log(numbers2)
# print(result)

multi_numbers1=numbers1.reshape(2,3)
multi_numbers2=numbers2.reshape(2,3)
print(multi_numbers1)
print("--------------------------")
print(multi_numbers2)
print("--------------------------")
result=np.vstack((multi_numbers1,multi_numbers2)) #matrisleri vertical(dikey) olarak ekler 
result=np.hstack((multi_numbers1,multi_numbers2)) #matrisleri horizontal(yatay) olarak ekler
print(result)
print("--------------------")
print(numbers1)
print(numbers2)
result=numbers2>=50 #numbers2 içindeki değerlerden 50 den buyuk olanlar true dierleri false 
# [True False True True...] gibi

result=numbers2%2==0 #çift olanlar True dierleri False [True True False...] gibi

print(numbers2[result]) #Resultun içinde çift olanlar True çevirdi. Resultu tekrardan 
#numbers 2 ye yollayınca sadece True olan indexlerdeki verileri aldık.
print(result)
