from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import requests
from bs4 import BeautifulSoup
### requests 로 정보 가져오기
# url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=false"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
#     'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")
# with open("C:/workspace/smclass/c1023/yeogi1.html","w",encoding="utf-8-sig") as f:
#   f.write(soup.prettify())
# data = soup.select_one("div.css-1qumol3")
# print(data)

## seleninum
# 파일 저장해서 불러오기 1회
for i in range(5):
  url = f"https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=false&page={i+1}"
  # # webdriver.Chrome(드라이버주소/chromedriver.exe)
  # # root에 파일이 저장되어 있으면 주소 입력하지 않아도 됨.
  # browser = webdriver.Chrome()
  # # 이동하려는 주소입력
  # browser.get(url)
  # time.sleep(3)
  # soup = BeautifulSoup(browser.page_source,"lxml")

#   # 파일에 저장
#   with open(f"C:/workspace/smclass/c1023/yeogi{i+1}.html","w",encoding="utf-8-sig") as f:
#     f.write(soup.prettify())



# # 세인트존스 제목, 평점, 평가수, 가격, 이미지 주소, 링크주소
# 평점 9.0이상, 평가수 500이상, 금액 12만원 이하만 출력
# 파일 5개를 모두 검색해서 출력


# print(lists)
print("[강릉숙소]")

# 파일 불러오기 - BeautifulSoup 으로 파싱
for i in range(5):
  with open(f"C:/workspace/smclass/c1023/yeogi{i+1}.html","r",encoding="utf-8-sig") as f:
    soup = BeautifulSoup(f,'lxml')

data = soup.select_one("div.css-1qumol3")
sells = data.select("a")

for idx,sell in enumerate(sells):
  try:
    price = int(sell.select_one("span.css-5r5920").text.strip().replace(",",""))
    rating = float(sell.select_one("div.css-wtzmcu").text.strip())
    num = int(sell.select_one("span.css-oj6onp").text.strip().replace(",","")[:-4])

    if num > 500 or rating<9.0 or price<1200000:
      print(f"{(i*20)+idx+1}.")
      print("숙소명 :",sell.select_one("h3").text.strip())
      print("평점 :",rating)
      print("평가수 :",num)
      print("금액 :",price)
      link = sell['href']
      print("링크 :","https://www.yeogi.com/"+link)
      print("*"*60)
    else:
      print(f"{idx+1}")
      print("제외")
      print("*"*60)
  except Exception as e:
    print("예외처리",e)