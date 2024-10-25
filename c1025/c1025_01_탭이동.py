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


# 1.
# https://www.naver.com/
# 네이버 쇼핑 검색창 입력 enter키 입력
# 네이버 쇼핑 클릭
# 네이버 쇼핑에서 무선마우스 검색창 입력 enter키 입력

url = "https://www.naver.com/"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)
time.sleep(1)

# 네이버
elem = browser.find_element(By.XPATH,'//*[@id="query"]')
elem.send_keys("네이버 쇼핑")
time.sleep(3)
elem.send_keys(Keys.ENTER)
time.sleep(1)
browser.find_element(By.XPATH,'//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a/mark').click()
time.sleep(1)

# 네이버 쇼핑에서 무선 마우스 검색창 입력 enter키 입력
# 새로운 탭으로 이동
browser.switch_to.window(browser.window_handles[1])
elem = browser.find_element(By.XPATH,'//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
elem.click()
time.sleep(2)
elem.send_keys("무선 마우스")
time.sleep(1)
elem.send_keys(Keys.ENTER)

input("enter키 입력완료")


# -------------------------------------------


