import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a) # 첫번째로 발견되는 a element 를 뿌려줘
#print(soup.a.attrs)
# print(soup.a["href"])

# print(soup.find("a" , attrs={"class" : "Nbtn_upload"}))
# print(soup.find(attrs ={"class" :"Nbtn_upload"}))

rank1 = soup.find("li",attrs={"class" : "rank01"})
# print(rank1.a)
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a)
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a)
# rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# print(rank1.find_next_siblings("li"))

webtoon = soup.find("a" , text="참교육")
print(webtoon)