import pandas as pd
import numpy as np

data=np.random.randint(10,100,15).reshape(5,3)

df=pd.DataFrame(data,index=["a","c","e","f","h"],columns=["column1","column2","column3"])

df=df.reindex(["a","b","c","d","e","f","g","h"])

newColumn=[np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"]=newColumn

result=df
result=df.drop(["column2","column3"],axis=1) #kolon silme
result=df.drop(["a","b"],axis=0) #satır silme
result=df.isnull() #boş olanları true 
result=df.notnull() #dolu olanlar true
result=df.isnull().sum() #boş olanların sayısı 1+1+1 True=1 oluğundan sum ile 3 verir
result=df["column1"].isnull().sum()

result=df[df["column1"].notnull()]

result=df[df["column1"].notnull()]["column1"]

result=df[df["column4"].notnull()]["column4"]

result=df.dropna() #axis=0 satır göre silme axis=1 stuna göre silme nan olanları siler
result=df.dropna(axis=1)
result=df.dropna(axis=0,how="any") #satırda 1 tane bile nan varsa satırı siler
result=df.dropna(axis=0,how="all") #satırda hepsi nan ise satırı siler
result=df.dropna(subset=["column1","column2"],how="all") #kolon 1 ve 2 de 2 değerde non ise satırı siler
result=df.dropna(subset=["column1","column2"],how="any") #kolon 1 ve 2 de 1 tane si nan olsa satırı siler
result=df.dropna(thresh=4) #en az sayıda normal veri 4 tane normal veri varsa satırı tutar


result=df.dropna(thresh=1) #en az sayıda normal veri 1 tane normal veri varsa satırı tutar

result=df.fillna(value="no input") #NaN olan yerleri no input yazar
result=df.fillna(value="1") #NaN olan yerleri 1 yazar
#df.fillna(value="") ile NaN olan yerlere ortalama değer yazmk istenebilir bunun için fonksiyon tanımlnır
result=df.sum() #kolonların değerlerinin toplamı
result=df.sum().sum() #df içindeki tüm verilerin toplamı
result=df.size #NaN olan değerlerle berber toplm elemn sayısı
result=df.isnull().sum() #kolonlardaki toplam NaN olan değer sayısı
result=df.isnull().sum().sum() #df içindeki toplm NaN olan değerlerin sayısı
def ortalama(df):
    toplam=df.sum().sum()
    size=df.size-df.isnull().sum().sum()
    return toplam/size
result=df.fillna(value=ortalama(df))

# print(df)
# print(result)