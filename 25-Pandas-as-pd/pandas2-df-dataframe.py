#Data Frame birden fazla serinin bir araya gelmesiyle oluşur

import pandas as pd


liste=[["Ahmet",50],["Mehmet",80],["Furkan",100]]
df=pd.DataFrame(liste, columns=["Name","Grade"], index=[1,2,3], dtype=float)
print(df)
dictionry={"Name": ["ahmet","mehmet","furkan"],"Grade":[40,50,70]}
df=pd.DataFrame(dictionry)
print(df)




# s1=pd.Series([3,2,0,1])
# s2=pd.Series([0,3,7,2])

# data=dict(apples=s1, oranges=s2)

# df=pd.DataFrame(data)
# print(df)