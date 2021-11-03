#Son dk Haberleri Api uygulaması 1000request weekly
import requests

headlines_url="https://newsapi.org/v2/top-headlines"
everything_url="https://newsapi.org/v2/everything"
api_key="4d9be3b8b43f4a34a6be2c3926d78e97"
# response=requests.get(headlines_url, params={
#     "apiKey": api_key,
#     "country": "tr"
# })
response=requests.get(everything_url, params={
    "apiKey": api_key,
    "q": "fenerbahçe",
    "language": "tr",
    "sortBy": "publishedAt",
    "pageSize": 10
})

haberler= response.json()["articles"]

for i in haberler:
    print(i["source"]["name"])
    print(i["title"])
    print(i["url"])
    print(i["publishedAt"])