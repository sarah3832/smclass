# 구글드라이버 -> chromedriver window64 다운로드
# selenium : 웹 페이지 자동화 (동적 웹 페이지o) / 속도가 느림
# ------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup

# Chrome() : ()안에 chromedriver.exe 위치지점을 입력해 줘야함
# root에 파일이 저장되어 있으면 입력하지 않아도 됨
browser = webdriver.Chrome()
browser.get("https://naver.com")

# html 위치찾기 - requests:select
elem = browser.find_element(By.CLASS_NAME,'MyView-module__link_login___HpHMW')
elem.click()  # 클릭
browser.back()  # 뒤로가기
browser.forward()  # 앞으로가기
browser.refresh()  # 새로고침
elem = browser.find_element(By.NAME,'pw')


elem = browser.find_element(By.ID,"query")
# 글자 입력
elem.send_keys("네이버 영화")
# enter키 입력
elem.send_keys(Keys.ENTER)
# 클릭
elem.click() 

# 새창 이동
browser.switch_to.window(browser.window_handles[1])



time.sleep(100)  # 지연시켜 줌
