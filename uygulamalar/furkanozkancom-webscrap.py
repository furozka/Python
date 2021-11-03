import requests
from bs4 import BeautifulSoup
import csv

url="http://furkanozkan.com/"
html_doc=requests.get(url)

soup=BeautifulSoup(html_doc.text,"html.parser")

with open("furkanozkan.csv","w",encoding="UTF-8",newline="") as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(["Article Name","Article Link"])
    articles=soup.find_all("article",class_="type-post")
    for article in articles:
        article_links=article.find_all("a")
        article_link=article_links[0]["href"]
        article_head=article_links[1].text
        csv_writer.writerow([article_head,article_link])
