plakalar = {'kocaeli': 41,'istanbul': 34}
print(plakalar["kocaeli"])
plakalar['rize']=53
print(plakalar)
plakalar["izmir"]=35
print(plakalar)
##################################
ogrenciler = {1: {"yaş":25,"isim":"furkan","meslek":"mühendis"},2: {"yaş":24,"isim":"süleyman","meslek":"mühendis"}}
print(ogrenciler[1])
print(ogrenciler[1].values())
print(ogrenciler[2].keys())
print(ogrenciler[2]["isim"])