def dateNowYear():
    import datetime
    return datetime.datetime.now().year

def ageCalculate():
    tarih=int(input("Doğum tarihiniz: "))
    yas=dateNowYear()-tarih
    print(f"Yaşınız: {yas}")

def dateNowHour():
    import datetime
    return datetime.datetime.now().hour

def selamla():
    if 12<dateNowHour()<18:
        print("İyi günler")
    elif 5<dateNowHour()<12:
        print("Günaydın")
    elif dateNowHour()>18 and dateNowHour()<24:
        print("iyi akşamlar")
    else:
        print("iyi geceler")

selamla()

print(dateNowHour())
ageCalculate()