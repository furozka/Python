import requests
import datetime
url="http://api.weatherapi.com/v1"
api_key="721fc0c88cce469491a111808211605"
current_url="http://api.weatherapi.com/v1/current.json"
forecast_url="http://api.weatherapi.com/v1/forecast.json" #Gelecek guler tahmin

sehir=input("Hava durumu için şehir bilgisi giriniz: ")

response = requests.get(current_url, params={
    "key": api_key,
    "q": sehir,
    "lang": "tr"
})

sonuc= response.json()
sehir=sonuc["location"]["name"]
havadurumu=sonuc["current"]["temp_c"]
durum_text=sonuc["current"]["condition"]["text"]
print(f"{sehir} şu anda {havadurumu} derece ve {durum_text}." )