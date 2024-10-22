import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# 순위, 사진링크주소, 제목, 가수명
data = soup.select_one("#frm > div > table")
tits = data.select("tr>th")
title = []

for tit in tits:
  title.append(tit.text)
  print(tit.text,end="\t")
print()
print("-"*100)



td_lists = []
for i in range(1,101):
  td_list = []
  print(data.select("lst50"))