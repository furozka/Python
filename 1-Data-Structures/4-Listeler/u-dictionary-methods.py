'''
    player 1: 
        id           => 1
        name         => Cristiano Ronaldo
        yearOfBirth  => 1985
        nationality  => Portugal
        current_team => Portugal
        history      => Juventus,Real Madrid,Portugal

    player 2: 
        id           => 2
        name         => Lionel Messi
        yearOfBirth  => 1987
        nationality  => Argentina
        current_team => Barcelona,
        history      => Barcelona,Argentina,Portugal
'''

# 1- Yukarıda verilen bilgileri liste içerisinde saklayınız.
playercount=int(input("oyuncu sayısını giriniz: "))+1
players={}
for x in range(1,playercount):
    id=int(input("id: "))
    name=input("Name: ")
    yearOfBirth=input("Born Year: ")
    nationality=input("Nationality: ")
    team=input("Current Team: ")
    history=input("History: ")
    players[id]={"Name": name,"Year":yearOfBirth,"Nationality":nationality,"Team":team,"History":history}
print(players)