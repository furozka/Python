from bs4 import BeautifulSoup
import csv
import requests
from requests.models import encode_multipart_formdata

url="https://sadikturan.com/"

html_doc=requests.get(url)

soup=BeautifulSoup(html_doc.text, "html.parser")
kurslar=soup.select(".kurs")
with open("kurslar.csv","w",newline="",encoding="UTF-8") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["kurs adi","kurs image","kurs aciklama","udemy linki","site linki"])
    for kurs in kurslar:
        kurs_adi=kurs.h2.string
        kurs_img=kurs.img["src"]
        kurs_aciklama=kurs.span.string
        link=kurs.find(class_="card-footer").find_all("div")[1].find_all("a")
        udemy_link=link[0]["href"]
        kurs_site_link=link[1]["href"]
        print(kurs_adi,"\n",kurs_img,"\n",kurs_aciklama,"\n",udemy_link,"\n",url+kurs_site_link)
        csv_writer.writerow([kurs_adi,kurs_img,kurs_aciklama,udemy_link,url+kurs_site_link])