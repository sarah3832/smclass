from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests
from bs4 import BeautifulSoup
import random
from selenium.webdriver.chrome.options import Options

# ------------------------------------------
# selenium 화면을 숨김처리
options = Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
# ------------------------------------------

# 노트북 검색 된 사이트 1,2,3페이지에서
# 만족도는 95이상, 평가수 100이상, 금액 1500000이하 검색
url = "https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81&k=61&p=1"
# 브라우저 열기
browser = webdriver.Chrome()
# 창 최대화
browser.maximize_window()
# url입력
browser.get(url)


soup = BeautifulSoup(browser.page_source,"lxml")

# 기준점
data = soup.select_one("div.section__module-wrap").text

print("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36")
print(data)
browser.get_screenshot_as_file("gmarket.png")
input("엔터키 입력완료")


# # html저장하기
# with open('C:/workspace/smclass/c1024/gmarket.html','w',encoding='utf-8') as f:
#   f.write(soup.prettify())
# input("Enter키를 입력하면 완료됩니다.")

# 파일불러와서 soup으로 파싱
# with open('C:/workspace/smclass/c1024/gmarket.html','r',encoding='utf-8') as f:
#   soup = BeautifulSoup(f,"lxml")


# lists = data.select("div.box__item-container")
# print(len(lists))

# print("[ 페이지 1 ]")



