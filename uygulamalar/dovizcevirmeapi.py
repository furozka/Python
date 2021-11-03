import requests
url_convert="http://api.exchangeratesapi.io/v1/latest"
api_key="2b0f272c86a69705d75ebf6d176675ec"

dovizturu=input("Verilen Doviz türünü girin: ")
alinandoviz=input("Alınan Döviz türünü giriniz: ")
miktar=int(input(f"Ne kadar {dovizturu} bozdurmak istiyorsunuz: "))

response=requests.get(url_convert, params={
    "access_key": api_key,
    "base": dovizturu
})
sonuc=response.json()
print(sonuc)
rate=sonuc["rates"][alinandoviz]
print(f"1 {dovizturu} = {rate} {alinandoviz}")
print(f"{miktar} {dovizturu} = {rate*miktar} {alinandoviz}")


