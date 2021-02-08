import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text , "lxml")
cartoons = soup.find_all("a", attrs={"class" : "title"})
#soup 객체 전체에서 태그명이 a 이고 class 명이 title 인 모든 a 를 가져온다 .

for cartoon in cartoons:
    print(cartoon.get_text())

    