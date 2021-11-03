import pandas as pd
import numpy as np

data={
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bca","ade","cba","dea"]
}

def kareAl(x):
    return x*x

kareal2=lambda a: a**2

df=pd.DataFrame(data)


result=df
result=df["Column2"].unique() #tekrrlayanlrı 1 kere yazar liste halinde elemanları getirir
result=df["Column2"].nunique() #unique eleman sayısını getirir
result=df["Column2"].value_counts() #her elemanın kaç kez tekrarlandığı
result=df["Column1"]**2 #kolon 1 deki elemanlrı 2 ile çarpar bunun yerine fonksiyon kullnılabilir
result=df["Column1"].apply(kareAl) #fonksiyon kullanarak kre aldık
result=df["Column1"].apply(kareal2) #lmbda fonksiyonla tanımlı fonksiyon kullanarak kare alma
result=df["Column1"].apply(lambda a: a**2) #direk apply içinde tanımlı kare alma
result=df["Column3"].apply(len) #satırdaki eleman sayıları
df["Column4"]=df["Column3"].apply(len) #satır eleman sayılarını başka kolona aktardık

result=len(df.columns) #kaç kolon oldugu
result=df.index #index bilgisi 0 dan baslar 5 e kadar gider 1 er artar seklinde
result=len(df.index) #index uzunluğunu verir 0 dan  5 e kadar = 5
result=df.info #bilgi verir

result=df.sort_values("Column2") #kolon 2 yi küçükten üyüğe sıralar
result=df.sort_values("Column3")
result=df.sort_values("Column2", ascending=False)["Column2"] #kolon 2 yi büyükten küçüğe doğru sıralar

data = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df=pd.DataFrame(data)
df=df.pivot_table(index="Ay",columns="Kategori",values="Gelir")

print(df)
