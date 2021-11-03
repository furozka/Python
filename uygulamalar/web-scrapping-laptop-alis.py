import requests
from bs4 import BeautifulSoup
from soupsieve.css_parser import PSEUDO_COMPLEX_NO_MATCH
from decimal import Decimal

url="https://www.n11.com/bilgisayar/dizustu-bilgisayar"

response=requests.get(url)

max_price=int(input("Enter your max price: "))

soup=BeautifulSoup(response.content,"html.parser")

computers=soup.find_all("li",class_="column")


for computer in computers:
    if computer.find("h3",class_="productName")!=None:
        computer_name=computer.find("h3",class_="productName").text.lstrip()
    if computer.find("div",class_="proDetail").find("del")!=None:
        previous_price=computer.find("div",class_="proDetail").find("del").text.strip("TL")
    if computer.find("input",class_="productDisplayPrice")!=None:
        now_price=computer.find("input",class_="productDisplayPrice")["value"]
    
    if computer.find("div",class_="proDetail").find("span",class_="ratio")!=None:
        indirim_oranı=computer.find("div",class_="proDetail").find("span",class_="ratio").text
    # indirim=indirim_oranı*int(previous_price)
    satici_linki=computer.find("div",class_="pro").a["href"]
    print(f"{computer_name}\nBefore price: {previous_price} %{indirim_oranı}= indirim:\nNow Price: {now_price}\nSatici: {satici_linki}")
    print("*".center(100,"*"))