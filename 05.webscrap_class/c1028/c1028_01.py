# [ 프로그램 설치 방법 ]
# 1. 파이썬 다운로드
# python 설치
# 환경변수 path 설정

# 2. 라이브러리 설치
# pip install requests
# pip install beautifulsoup4
# pip install lxml

# 3. selenium 설치
# ## chromedriver 크롬 드라이버 다운로드
# https://chromedriver.chromium.org/downloads

# 4. 오라클 라이브러리 설치
# python -m pip install oracledb

import oracledb

# oracle 연결 - sql developer 연결
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
# 연결확인
print(conn.version)

# sql실행창 오픈
# 1개 검색된 데이터내용 호출
# cursor = conn.cursor()
# sql = "select count(*) from member"
# cursor.execute(sql)
# count1 = cursor.fetchone()
# print("개수 : ",count1)

# 여러개 검색된 데이터내용 호출
cursor = conn.cursor()
sql = "select * from member"
cursor.execute(sql)
rows = cursor.fetchall()

# for row in rows:
#   print(row)

# print(rows[0][0],rows[0][1],rows[0][2],rows[0][3])


title = ['id','no','name','email','phone','gender','hobby','datetime']
for i in title:
  print(f"{i:15}",end='\t')
print()
print("-"*140)

for row in rows:
  for j in range(len(title)):
    print(f"{row[j]:10}",end='\t')
  print()

conn.close()