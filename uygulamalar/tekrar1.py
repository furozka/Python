""" Değişken Tanımlama """
# a=5
# b="furkan"
# for i in b:
#     print(i)
#--------------------------
""" Data Types """
# a=6.87651684
# print(a)
# print(round(a,2))
#-------------------------
""" Strings """
# a="furkan"
# print(a[0])
# print(a[::])
# print(a[::-1])
# print(a[:3])
# print(a[3:])
# print(len(a))
# #------------------------
""" String Format """
# a="furkan"
# b="ozkan"
# age=26
# print(f"{a} {b} {age}")
# print("{n} {s} {a}".format(n=a,s=b,a=age))
#------------------------------
""" String Methods """
# yazi="benim Adım fuRkan OZkan yaşım 26"
# print(yazi.upper())
# print(yazi.lower())
# print(yazi.capitalize())
# print(yazi.center(50,"*"))
# print(yazi.find("Adım"))
# print(yazi.isalnum())
# print(yazi[:5].isalpha())
# print(yazi.split(" "))
# liste_yazi=yazi.split(" ")
# print(liste_yazi)
# print(yazi.strip("benim26 "))
# a=" ".join(liste_yazi)
# print(a)
# print(yazi.index("Ad"))
# yazi=yazi.replace("fuRkan","Furkan")
# print(yazi)
# print(yazi.startswith("benim"))
# print(yazi.endswith("36"))
# print(yazi.upper().isalpha())
# -----------------------------------
""" Listeler """
# a= "furkan ozkan 26"
# a_liste=a.split(" ")
# print(a_liste)
# print(a_liste[0])
# print(a_liste[1][2:])
# for i in a_liste:
#     print(i)
# ------------------------------------
""" Liste Methodları """
# a="Furkan Özkan 26"
# a_liste=a.split(" ")
# okul="Ankara EEE"
# a_liste.append("Engineer")
# a_liste.append(okul)
# print(a_liste)
# a_liste.remove(okul)
# print(a_liste)
# a_liste.pop(1)
# print(a_liste)
# a_liste.insert(2,"Yes")
# print(a_liste)
# print(a_liste.index("Yes"))
# sayilar=[1,10,4,9,7,6,3]
# sayilar.sort(reverse=1)
# print(sayilar)
# sayilar.clear()
# print(sayilar)
# a_liste.clear()
# print(a_liste)
# ----------------------------
""" Tuples """
# a,b=(1,3)
# print(a)
# print(b)
# print("-".center(50,"-"))
# tuplee=(1,3,5,7,8,9)
# listee=list(tuplee)
# print(listee)
# tuplee=tuple(listee)
# print(tuplee)
# -----------------------------
""" Dictionaries """
# sozluk=[]
# def ekle(sozluk,name,surname,age,count=1):
#     print("sozluge kişi ekleniyor.")
#     for _ in range(count):
#         sozluk.append(
#             {"isim": name,
#             "soyad": surname,
#             "yaş": age}
#         )
#     print(sozluk)
#     print(f"tanımlı kişi sayısı {len(sozluk)}")
# ekle(sozluk,"furkan","ozkan","26")
#--------------------------------
""" Koşullu İfadeler """
#---------------------------------
""" Döngüler """
#----------------------------------
""" Döngü Methodları """
# for i in range(10):
#     print(i)
# liste =["furkan","ahmet","Veli"]
# for i in enumerate(liste,1):
#     print(i)

# liste2=[5,6,7,8]
# liste3=list(zip(liste,liste2))
# print(liste3)
# --------------------------------
""" List Comprehension """
# liste=[i**2 for i in range(10)]
# print(liste)

# liste1=[i for i in range(10) if i%2==0]
# print(liste1)

# liste2=[i if i%2==1 else ("çift") for i in range(10)]
# print(liste2)
#-------------------------------------
""" Fonksiyonlar """
# def toplama(*args, **kwargs):
#     return sum(args)

# print(toplama(3,5,4,7,5,5,5))

# def ortak_selam(fn):
#     def wrapps(*args,**kwargs):
#         print("oooooooo")
#         return(fn(fn(*args,**kwargs)))
#     return wrapps

# @ortak_selam
# def selamlama(isim="furkan"):
#     return f"merhaba {isim}"
# print(selamlama())
# print(selamlama("ali"))
#-------------------------------------
""" Lambda Fonksiyonu """
# kare_Al=lambda a: a**2
# print(kare_Al(4))
# print(kare_Al(3))
# def ust_Al(num):
#     return lambda a: a**num

# ust5=ust_Al(5)
# print(ust5(2))

# multiply=lambda a,b: b*a
# print(multiply(3,5))

# toplama=lambda *args: sum(args)
# print(toplama(3,5,7,8,9,8,45))
# -----------------------------------
""" Map Fonksiyonu """
# liste=[1,2,3,-4,5,6,7]
# print("ali".center(100,"*"))
# print(list(map(lambda a: a**2,liste)))
# print(list(map(str,liste)))
# print(list(map(int,liste)))
# print(list(map(float,liste)))
# -----------------------------------
""" Filter Fonksiyonu """
# liste=[-1,-5,4,6,7,"a","5"]
# print(list(filter(lambda a: a%2==0,liste)))
# print(list(filter(lambda a: a<0,liste)))
#------------------------------------
""" Any-All """
# liste1=[0,0,1]
# liste2=[1,1,1]
# print(any(liste1)) #1 tane True olsa yeter
# print(any(liste2))
# print(all(liste1)) #hepsi true olmakzorunda
# print(all(liste2))
#--------------------------------------
""" Sorted Fonksiyonu """
#ana listeyi değiştirmeden sort eder
# liste=[9,15,1,70,5,7,13,4]
# sorted_liste=sorted(liste)
# reverse_sorted_liste=sorted(liste, reverse=1)
# print(liste)
# print(sorted_liste)
# print(reverse_sorted_liste)
#-------------------------------------
""" Min-Max """
# liste=[1,5,7,8,9,5,74,61,-5]
# print(max(liste))
# print(min(liste))
#------------------------------------
""" Sum-Round """
# liste=[1,5,7,8,9,5,74,61,-5]
# print(sum(liste))
# a=5.784651651
# print(round(a,2))
# ----------------------------------
""" Hata Yonetimi Debugging Try-Except """
# try:
#     a="furkan"
#     int(a)
# except Exception as ex:
#     print(ex)

# def toplama(a,b):
#     if a<0 or b<0:
#         raise ValueError("Values must be positive")
#     return a+b
        
# try:
#     print(toplama(-5,5))
# except Exception as ex:
#     print(ex)

# def isim_al():
#     isim=input("isminizi girin: ")
#     turkce=["ı","İ","ü","ö","ç","ş","ğ"]
#     for i in isim:
#         if i in turkce:
#             raise ValueError("isim turkce karekter iceremez")
#     if isim.isdecimal():
#         raise TypeError("isim yazıdan oluşmalı")
    
#     return isim
# try:
#     print(f"hoşgeldiniz {isim_al()}")
# except Exception as ex:
#     print(ex)
# ----------------------------------
""" PDB Debugging """

# def faktoriel(max):
#     import pdb; pdb.set_trace()
#     if max==1:
#         return 1
#     return max*faktoriel(max-1)

# print(faktoriel(10))
# ------------------------------
""" Math Modülü """
# import math
# a=5
# print(math.ceil(5.1))
# print(math.factorial(10))

# from math import comb
# print(comb(5,2))

# from math import *
# import math
# print(dir(math))
# print(help(math))
#-----------------------------------
""" Random Modülü """

# import random
# print(random.random())

# from random import randint
# print(randint(1,100))

# from random import *
# liste=["a","b","c","d"]
# print(liste)
# print(choice(liste))
# shuffle(liste)
# print(liste)
# sampled=sample(liste,3)
# print(sampled)
# for i in sampled:
#     liste.remove(i)
# print(liste)
# ---------------------------
""" Datetime Modülü """
# from datetime import date, datetime
# simdi=datetime.now()
# simdic=datetime.timestamp(simdi)
# simdiv=datetime.ctime(simdi)
# simdib=datetime.strftime(simdi,"%A %b %X %H %M %S")
# print(simdi)
# print(simdic)
# print(simdiv)
# print(simdib)
# ----------------------------
""" Os Modülü """
import os
# print(os.name)
# print(os.getcwd())
# print(os.mkdir("yeni dosya"))
# os.chdir("D://yazilim/Python/Python48saat/çalışmalar")
# print(os.listdir())
# print(os.stat("CardGame.py"))
# result=os.stat("CardGame.py")
# size_card=result.st_size/1024
# olusturulma_card=result.st_ctime
# from datetime import datetime
# print(size_card)
# print(olusturulma_card)
# olusturulma_card=datetime.fromtimestamp(olusturulma_card)
# print(olusturulma_card)
# os.rmdir("yenii")
# os.rmdir("yeni dosya")
# -----------------------------------------------------------
""" OOP #1 """