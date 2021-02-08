import requests
res = requests.get("http://google.com")
# res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()
# print("responce_Code: " , res.status_code) # 200(normal)

# if res.status_code == requests.codes.ok:
#     print("normal")
# else:
#     print("Error [errorcode ",res.status_code,"]")

# res.raise_for_status()
# print("web scraping running")

print(len(res.text))
print(res.text)

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)