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
# email 발송관련
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


# ----------------------------------------------------

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

# csv 파일저장
f = open('C:/workspace/smclass/c1025/newsranking.text','w',encoding='utf-8-sig',newline="")

# 기준점
data = soup.select_one("div.rankingnews_box")
lists = data.select("ul.rankingnews_list>li")
# print(len(lists))

for i,list in enumerate(lists):
  # print(f"{i+1}.",end=" ")
  title = list.select_one("div.list_content>a").text.strip()
  # print(title,end=" ")

  n_time = list.select_one("span.list_time ").text.strip()
  # print(n_time)

  n_list = [str(i+1),title,n_time] 
  # n_list.append(str(i+1))
  # n_list.append(title)
  # n_list.append(n_time)
  ",".join(n_list)
  # print(",".join(n_list))

  f.write(",".join(n_list)+"\n")

f.close()


# -----------------------------------------------

# 메일 보내기
smtpName = "smtp.naver.com"
smtpPort = 587

sendEmail = "sarah3832@naver.com"
pw = "PN7T8EJQYS3Q"
recvEmail = "sarah3832@naver.com"

title = "제목 : 네이버 뉴스 랭킹"
content = "파일을 첨부합니다."

msg = MIMEMultipart()
msg["Subject"] = title
msg["From"] = sendEmail
msg["To"] = recvEmail

# 파일 첨부
with open("C:/workspace/smclass/c1025/newsranking.text","rb") as f:
  attachment = MIMEApplication(f.read())  # 파일첨부
  attachment.add_header('Content-Disposition','attachment',filename="newsranking.text")
  msg.attach(attachment)

s = smtplib.SMTP(smtpName,smtpPort)
s.starttls()  # 보안인증
s.login(sendEmail,pw)
s.sendmail(sendEmail,recvEmail,msg.as_string())
print("msg :")
print(msg.as_string())
s.quit()

print("메일이 발송되었습니다.")

