# flight.html 금액이 50000원 미만인 항공권을 출력하시오.
# 김포-제주 80000원 이하 항공권 개수 
# 제주-김포 80000원 이하 항공권 개수 
import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/smclass/c1023/flight.html"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
soup = BeautifulSoup(res.text,"lxml")
data = soup.select_one("div.flicking-camera")
sells = data.select("div.statsRecommendedHotels_item__YicDV")

with open('C:/workspace/smclass/c1023/flight.html','r',encoding='utf-8') as f:
  soup = BeautifulSoup(f,'lxml')


for idx,sell in enumerate(sells):
  try:
    price = int(sell.select_one("b.statsRecommendedHotels_value__SWAMT").text.strip().replace(",",""))

    if price > 80000:
      print(f"{idx+1}.")
      print("숙소명 :",sell.select_one("div.statsRecommendedHotels_name__ZhGuX"))
      print("평점 :",sell.select_one("b.statsRecommendedHotels_rate__FiTxw statsRecommendedHotels_item_info__EWxt9"))
      print("가격 :",price)


  except Exception as e:
    print("예외처리",e)



    


