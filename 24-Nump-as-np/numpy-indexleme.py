import numpy as np

numbers1=np.array([0,5,10,15,20,25,50,75])
result=numbers1[0:5]
result=numbers1[3:]
result=numbers1[::2]
result=numbers1[::-1]
result=numbers1[::-2]

numbers2=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(numbers2)
result=numbers2[0] #sıfırınca satır [1 2 3]
result=numbers2[0,2] #0. satırın 2. indeksi 3
result=numbers2[:,2] #tüm satırlardan 2. indeksi alır [3 6 9]
result=numbers2[:,0:2] #tüm satırlarda 0 ve 1. indeksi alır [[1,2],[4,5],[7,8]]
result=numbers2[-1,:] #son satırdan baslar sona kadar [7 8 9]
result=numbers2[:2,:2] #ilk 2 satırı seçer onlardanda ilk 2 indexi alır [[1 2],[4,5]]
# print(result)

arr1=np.arange(10)
arr2=arr1.copy() #arrayı kopyalama

arr2[0]=20
print(arr1)
print(arr2)