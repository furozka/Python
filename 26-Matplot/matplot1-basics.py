import matplotlib.pyplot as plt
import numpy as np

# x ve y ye gore grafik çizdirme
""" Örnek 1 
x=[1,2,3,4]
y=[i**2 for i in x]
plt.plot(x,y,"o--r") #x ve y yi kesisim noktalarında yuvarlar kırmızı isaretler ve kesikli çizgilerle birlestirir
plt.axis([0,6,0,20])
plt.title("Grafik Başlığı")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show() 
"""

# label isimleri sol üstte gosterme plt.legend() ile
""" Örnek 2
x=np.linspace(0,2,100)

plt.plot(x, x, label="x",color="red") #x i çizer label olarak x renk kırmızı label sol üstte plt.legend() ile gost.
plt.plot(x, x**2, label="x**2",color="yellow") #x**2 çizer
plt.plot(x, x**3, label="x**3",color="green") #x**3 çizer
plt.xlabel("x label") #x labeli isim
plt.ylabel("y label") #y labeli isim
plt.title("Simple plot") #baslik
plt.legend() #sol ustte çizim labelleri gosterilir
plt.show() #çizimi gosterir
 """

# birde fazla grafik çizdirme subplot()
""" Örnek 3
x=np.linspace(0,2,100)
fig,axs=plt.subplots(3) #3 adet grafik çizmeye yarar
axs[0].plot(x,x ,color="red")
axs[0].set_title("linear")
axs[1].plot(x,x**2, color="yellow")
axs[1].set_title("quadratic")
axs[2].plot(x,x**3,color="green")
axs[2].set_title("cubic")
plt.tight_layout()
plt.show()  
"""

#bire fazla fig,axs=plt.subplot(2,2) plt.suptitle()
""" Örek 4
x=np.linspace(0,2,100)
fig,axs=plt.subplots(2,2)
fig.suptitle("Grafik baslıgı")
axs[0,0].plot(x,x,color="red")
axs[0,0].set_title("birinci")
axs[0,1].plot(x,x**2,color="yellow")
axs[0,1].set_title("ikinci")
axs[1,0].plot(x,x**3,color="green")
axs[1,0].set_title("ucuncu")
axs[1,1].plot(x,x**4,color="purple")
axs[1,1].set_title("dorduncu")
plt.tight_layout()
plt.show() 
"""


# Data Grafiği çizdirme
""" Örek 5 
import pandas as pd

df=pd.read_csv("ek\\nba.csv")
df = df.drop(["Number"], axis = 1).groupby("Team").mean()
df.head().plot(subplots=True)
plt.legend()
plt.show() 
"""
