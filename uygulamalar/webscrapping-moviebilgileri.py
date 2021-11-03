import requests
from bs4 import BeautifulSoup

chose=input("1- Most Popular Films\n2- Top Rated Films\nChose: ")
url_most_popular="https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
url_top_rated="https://www.imdb.com/chart/top/?ref_=nv_mv_250"
if chose=="1":
    url=url_most_popular
elif chose=="2":
    url=url_top_rated
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
movies=soup.find("tbody",class_="lister-list").find_all("tr")
# print(movies)
for movie in movies:
    movie_ranking=movie.find("td",class_="posterColumn").span["data-value"]+"."
    movie_name=movie.find("td",class_="titleColumn").find("a").text
    movie_actors=movie.find(class_="titleColumn").a["title"]
    movie_year=movie.find(class_="titleColumn").find(class_="secondaryInfo").text.strip("()")
    if movie.find("td",class_="imdbRating").strong!= None:
        movie_rating=movie.find("td",class_="imdbRating").strong.text
    else:
        movie_rating=movie.find("td",class_="imdbRating").text
    print(f"{movie_ranking} {movie_name.ljust(70,'-')}  Imdb: {movie_rating}  Year: {movie_year}\nActors: {movie_actors}")