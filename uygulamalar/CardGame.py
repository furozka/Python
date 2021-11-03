#kart oyunun
# sinek=club
# maça=spade
# karo=diamond
# kupa=hearth
import random
class Card:
    types=["club","spade","diamond","hearth"]
    values=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self, _type, _value):
        if _type not in Card.types or _value not in Card.values:
            raise ValueError("Undefined card value or type")
        self.type=_type
        self.value=_value
    
    def cardCome(self):
        return print(f"{self.type} {self.value}")
# try:
#     club5=Card("club","5")
#     print(club5)
#     club5.cardCome()
#     diamondA=Card("diamond","A")
#     diamondA.cardCome()
# except ValueError as ex:
#     print(ex)

class Desk:
    types=["club","spade","diamond","hearth"]
    values=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

    def __iter__(self):
        return self

    def __init__(self):
        self.cards=[]
        self.handed=[]
        for i in Desk.types:
            for j in Desk.values:
                self.cards.append([i,j])
                Card(i,j)
    
    def cardNumber(self):
        return len(self.cards)
    
    def cardShuffle(self):
        if self.cardNumber()<52:
            raise ValueError("Ouyn başladıktan sonra Deste Karıştırılamaz")
        random.shuffle(self.cards)
    
    def cardGive(self, _number):
        
        if _number>len(self.cards):
            raise ValueError(f"Destede {len(self.cards)} kart var")
        verilenler=self.cards[-_number::]
        for i in verilenler:
            self.cards.remove(i)
        for i in verilenler:
            self.handed.append(i)
        return verilenler
    
    def handCardGive(self):
        
        atilan=random.sample(self.handed,1)
        for i in atilan:
            self.handed.remove(i)
        return f"{atilan}"
print("".center(100,"*"))
deste1=Desk()
# deste2=Desk()
# deste3=Desk()
# print(deste1.cardNumber())
# deste1.cardShuffle()
# print(deste1.cards)
# print("Destedekiler".center(100,"*"))
# print(deste1.cardGive(5))
# print(deste2.cardGive(3))
# print("Kart verdikte sonra".center(100,"*"))
# print(deste1.cardNumber())
# print("Handed Cards".center(100,"*"))
# print(deste1.handed)
# print("Atılan Kart")
# print(deste1.handCardGive())
# print("Kart atıldıktan sonra handed")
# print(deste1.handed)
# print(deste2.handed)
for i in deste1.cards:
    print(i)
