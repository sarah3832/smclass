import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()  # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")
sum = 0

# print(soup.select_one("h3.h_popular>span").text)


# 기준점
data = (soup.select_one("#container > div.aside > div > div.aside_area.aside_popular"))

# 인기검색 종목
print(f"[ {data.select_one("span").text} ]")

# 1,2,3,4,5 위
pops = data.select("tbody>tr")
# print("개수 :",len(pops))

for pop in pops:
  print("회사명 : ",pop.select_one("tr>th").text)
  print("현재가 : ",pop.select_one("td").text)
  # 현재가의 합계를 구하시오.
  num = int(pop.select_one("td").text.replace(",",""))
  sum += num

  # next_sibling : 형제관계 / find_next_sibling : 형제관계 중 검색
  # print("변동 : ",pop.select_one("td").find_next_sibling("td").text)
  sps = pop.select_one("td").find_next_sibling("td").select("span")
  tit = ["변동","변동액"]
  for idx,sp in enumerate(sps):
    print(tit[idx],":",sp.text.strip())
  # print("변동1 : ",pop.select_one("td").find_next_sibling("td").select_one("span").text)
  # print("변동액 : ",pop.select_one("td").find_next_sibling("td").select_one("span").next.next.next.strip())
  print("-"*30)

print(f"합계 : {sum:,}")