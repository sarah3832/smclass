# requests 라이브러리 설치 (pip install requests) : 웹 정보 요청하는 라이브러리
# beautifulsoup4 라이브러리 설치 (pip install beautifulsoup4) : HTML 및 XML 파일에서 원하는 데이터를 손쉽게 Parsing 할 수 있는 python 라이브러리
# lxml 라이브러리 설치 (pip install lxml) : lxml을 설치하면 css문법으로 특정 요소를 쉽게 가져올 수 있는 python 라이브러리
# 웹 스크래핑 : 웹 사이트 상에서 원하는 정보를 추출하여 수집하는 기술

# ----------------------------------------------------------------------

# 웹 스크래핑 세팅
import requests
# res = requests.get("https://www.google.com/")  # html 소스를 가져옴
res = requests.get("https://www.naver.com/")  # html 소스를 가져옴
# res = requests.get("https://www.melon.com/index.htm")  # html 소스를 가져옴
res.raise_for_status()  # 에러 시 종료

# requests 정보를 가져올시 
# 제이쿼리, 자바스크립트, 외부페이지, react, vue .. 비동기식으로 작동되는 소스는
# 가져오지 못함.

print("총 문자 길이 :",len(res.text))

# print(res.text)  # html소스 출력  

# 웹 소스코드 파일 저장
# f = open("a.hmtl","w",encoding="utf-8")
# f.write(res.text)
# f.close()

# f.close() 생략
with open("C:/workspace/smclass/c1021/naver.html","w",encoding="utf-8") as f:
  f.write(res.text)


# if res.status_code == 200:
#   print(res.text)
# else:
#   print("접근할 수 없습니다.")

# print("응답코드 : ",res.status_code)  # 200 = 정보가 있음
# print(res.text) 
