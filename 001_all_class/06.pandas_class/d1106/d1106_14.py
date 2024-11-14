from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

# [ 영화순위 ]
# 1. 2020년~2023년 영화 내용을 저장하시오.
# - csv파일로 저장
# - 이미지 저장
# - 제목
# - 관객수 : 숫자입력
# 1,312 -> 1312
# - 날짜

url = "https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status() 

soup = BeautifulSoup(res.text,"lxml")

# url = "https://search.daum.net/search?w=tot&q=2023%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
# browser = webdriver.Chrome()
# # # 이동하려는 주소입력
# browser.get(url)
# soup = BeautifulSoup(browser.page_source,"lxml")

# # 파일에 저장
# with open("C:/workspace/smclass/d1106/movie_list.html","w",encoding="utf-8-sig") as f:
#   f.write(soup.prettify())

# 파일 불러오기
with open("C:/workspace/smclass/d1106/movie_list.html","r",encoding="utf-8-sig") as f:
  soup = BeautifulSoup(f,'lxml')
# ------------------------------------------------

data = soup.select_one("#mor_history_id_0 > div > div.flipsnap_view > div > div:nth-child(1) > c-flicking-item > c-layout > div > c-list-doc")
lists = data.select("li")
m2023_lists = []

for idx,list in enumerate(lists):
  m2023_list = []
  title = list.select_one("div.item-title").text.strip()
  num = int(list.select_one("p.conts-desc>a").text.strip().replace(",","").replace("누적 ","").replace("만명",""))*10000
  img = list.select_one("img")["src"]

  print("제목 :",title)
  print("관객수 :",num)
  print("이미지 :",img)
  



