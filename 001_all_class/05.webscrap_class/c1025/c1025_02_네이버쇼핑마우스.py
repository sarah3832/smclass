from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pyautogui
import time
import requests
from bs4 import BeautifulSoup
import random
import csv


# 1.상단타이틀. csv파일로 저장
# f = open('c1023/stock.csv','w',encoding='utf-8-sig',newline="")
# writer = csv.writer(f)
# st_list = [ st.text  for st in stocks[0].select("th") ]

# 2.
# 제목, 금액, 평점, 평가수, 찜 정보를 1-5페이지까지 가져와서
# 평점 4.8이상, 평가수 1000명이상 인 상품을 csv파일로 저장하고 출력하시오.

# --------------------------------------------------------

# # 파일 저장 
browser = webdriver.Chrome()
browser.maximize_window()
for i in range(1,6):
  url = f"https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex={i}&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
  browser.get(url)
  time.sleep(2)
  soup = BeautifulSoup(browser.page_source,"lxml")

  # 화면스크롤 내리기 반복
  prev_height = browser.execute_script("return document.body.scrollHeight")

  while True:
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(1)

    # 페이지 로딩되면서 길어진 길이 다시가져옴
    curr_height = browser.execute_script("return document.body.scrollHeight")

    # 페이지 스크롤해서 길이가 더 길어졌는지 확인
    if prev_height == curr_height:
      break
    # 더 길어졌으면, 이전길이에 현재길이 입력시킴
    prev_height = curr_height
  print("스크롤 내리기 완료")


  with open(f'C:/workspace/smclass/c1025/navershop{i}.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())
  time.sleep(2)
  
# --------------------------------------------------------

# 파일 불러오기

# with open('C:/workspace/smclass/c1025/navershop.html','r',encoding='utf-8') as f:
#   soup = BeautifulSoup(f,"lxml")

# # 기준점
# data = soup.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div")
# # 클래스 종류 2개 - adProduct_item_1zC9h, product_item__MDtDF
# pros = data.select("div.adProduct_item_1zC9h")
# # print(len(pros))


# for idx,pro in enumerate(pros):
#   print(idx,".")
#   if pro['class'][0] == 'adProduct_item_1zC9h':
#     title = pro.select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(1) > div > div.adProduct_info_area__dTSZf > div.adProduct_title__amInq > a")
#     print(title)
#   else:
#     print('product_item__MDtDF')
#     title = pro.select_one("")


# class - product_item__MDtDF 상품
# title = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(3) > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_title__Mmw2K > a").text
# print(title)
# price = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(3) > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_price_area__eTg7I > strong > span.price > span.price_num__S2p_v > em").text.strip().replace(",","")
# print(price)
# rating = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(3) > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_etc_box__ElfVA > a > span.product_grade__IzyU3").text.strip().replace("\n","").replace(" ","")[2:]
# print(float(rating))
# p_count = pros[0].select_one("#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div > div:nth-child(3) > div.product_inner__gr8QR > div.product_info_area__xxCTi > div.product_etc_box__ElfVA > a > em").text.strip().replace("\n","").replace(" ","")[1:-2]
# print(float(p_count)*10000)