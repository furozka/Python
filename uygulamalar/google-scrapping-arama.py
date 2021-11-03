import requests
from bs4 import BeautifulSoup


search_input=input("aramak istediğiniz kelime: ").replace(" ","+")
link="https://www.google.com/search?q="+search_input
# link="https://www.google.com/search?q="+"python"
headerParams = {"user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"}

response=requests.get(link, headers=headerParams)

soup=BeautifulSoup(response.content,"html.parser")
results=soup.find_all("div",class_="g")
for i in results:
    if i.a!= None:
        linkler=i.a
        link=linkler["href"]
        if linkler.h3!=None:
            h3bas=i.h3
            if h3bas.text!= None:
                print(i.h3.text,"\n",link)
