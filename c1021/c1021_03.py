# naver 파일저장, 리솜리조트 파일저장

import requests
# url = "http://naver.com"
# url = "http://www.resom.co.kr/resom/main/main.asp"
# url = "http://www.daum.net/"

# https 안되면 http
# url = [
#   "http://naver.com",
#   "http://www.resom.co.kr/resom/main/main.asp",
#   "http://www.daum.net/"
# ]

# url = ["http://www.coupang.com/"]

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
# for i in range(len(url)):
#   res = requests.get(url[i],headers=headers)
#   res.raise_for_status()

# with open(f"C:/workspace/smclass/c1021/{i}.html","w",encoding="utf-8") as f:
#   f.write(res.text)

# print("프로그램 종료!")


# ---------------------------------------------

# 쿠팡페이지 저장
url = "http://www.coupang.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
print(res.text)

with open("C:/workspace/smclass/c1021/coupang.html","w",encoding="utf-8") as f:
  f.write(res.text)

print("완료")
