import os
import requests
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# 제목, 금액, 평점, 평가수, 링크주소, 이미지주소
# 금액: 90만원이상 / 평점: 4.5이상 / 평가수: 100명이상

# 기준점
data = soup.select_one("#productList")
# print(data)

lists = data.select("li")
n_lists = []
for idx,list in enumerate(lists):
  n_list = []  # 제목,금액,평점,평가수,링크,이미지
  try:
    # price,rating,num 타입변경
    price = int(list.select_one("strong.price-value").text.replace(",",""))
    rating = float(list.select_one("em.rating").text)
    num = int(list.select_one("span.rating-total-count").text[1:-1])
    # 금액,평점,평가수 비교
    if price >= 900000 and rating >= 4.5 and num >= 100:
        print(f"[ {idx}번째 ]")
        link = "https://www.coupang.com"+list.select_one("a")['href']
        print("1. 링크주소 : ",link)
        title = list.select_one("div.name").text
        print("2. 제목 :",title)
        print("3. 금액 :",price)   
        print("4. 평점 :",rating)
        print("5. 평가 수 :",num)
        img = "https:"+list.select_one("img")['src']
        print("6. 이미지 : ",img)
        print("-"*60)
        n_list = [link,title,price,rating,num,img]
        n_lists.append(n_list)
    else:
       print(f"[{idx} 번째 ] : 제외")

  except Exception as e:
     print(f"{idx}:에러",e)
     pass
  

# print(n_lists)
  
while True:
   print("[ 노트북 비교 ]")
   print("1. 금액정렬")
   print("2. 금액역순정렬")
   print("3. 평점정렬")
   print("4. 평점역순정렬")
   print("0. 종료")
   print("-"*60)
   choice = input("원하는 번호를 입력하세요. >> ")
   if choice == "1":
      n_lists.sort(key=lambda x:x[2])
      print(n_lists)
   if choice == "2":
      n_lists.sort(key=lambda x:x[2],reverse=True)
      print(n_lists)
   if choice == "3":
      n_lists.sort(key=lambda x:x[3])
      print(n_lists)
   if choice == "4":
      n_lists.sort(key=lambda x:x[3],reverse=True)
      print(n_lists)
   if choice == "0":
      print("프로그램 종료")
    





# ----------------------------------------------------------------

# # 링크주소
# print("1. 링크주소 : https://www.coupang.com"+data.select_one("a")['href'])

# # 제목
# print("2. 제목 :",data.select_one("div.name").text)

# # 금액
# price = int(data.select_one("strong.price-value").text.replace(",",""))
# print("3. 금액 :",price)

# # 평점
# rating = float(data.select_one("em.rating").text)
# print("4. 평점 :",rating)

# # 평가 수
# num = int(data.select_one("span.rating-total-count").text[1:-1])  # 괄호를 없앰
# print("5. 평가 수 :",num)

# # 이미지주소
# print("6. 이미지 : https:"+data.select_one("img")['src'])