# Kendisine gönderilen 2 sayıdan hangisi büyük bulan fonksiyonu yazınız.
def buyukOlan(x,y):
    if x>y:
        return f"{x} daha buyuk"
    elif y>x:
        return f"{y} daha buyuk"
    else:
        return "Aynılar"
print(buyukOlan(2,3))
print(buyukOlan(x=4,y=1))
print(buyukOlan(y=10,x=10))
# Kendisine gönderilen bir string bilgi içinde her karakter kaçar kez tekrarlanmış bulunuz.
def letterRepeat(string):
    return {letter: string.count(letter) for letter in string}
sonuc=(letterRepeat("pokemon"))
print(sonuc)
# Kendisine gönderilen list, command, position ve value bilgilerine göre liste üzerinde güncelleme yapınız.
def listeGuncelle(list=[1,2,3],command="add",position=0,value=None):
    if command=="add":
        list.insert(position,value)
    elif command=="remove":
        list.pop(position)
    return list
oncekiList=[5,6,5,7,7]
print(listeGuncelle(oncekiList,"add",4,13))
print(listeGuncelle(oncekiList,"add",1,18))
print(listeGuncelle(oncekiList,"remove",5))
print(listeGuncelle(oncekiList,"remove",4))
# Kendisine gönderilen renk isimlerinden içinde "blue" rengi varsa True döndüren fonksiyonu yazınız.
def blueDetect(*args):
    if 'blue' in args:
        return "True"
    else:
        return "False"
sonuc=blueDetect("red","green")
print(sonuc)
sonuc=blueDetect("red","green","blue")
print(sonuc)