# 오라클db에서는 타입 결정
# 문자형(숫자) 타입 + 숫자 사칙연산 가능
# 파이썬에서 호출한 타입의 결과값이 어떻게되는지 확인

import oracledb

def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except exit as e: print("예외처리 : ",e)
  return conn

conn = connects()
cursor = conn.cursor()
## chartable : number,number,varchar2,varchar2
## chartable2 : number,number,number,number
sql = "select no,kor,to_char(kor_char,'00000000'),to_char(kor_mark,'999,999,999') from chartable2"
cursor.execute(sql)
rows = cursor.fetchall()

for row in rows:
  print(f"두수의 합 : {row[1]+row[2]}")  # 오라클에서는 계산가능, 파이썬 불가능
  print(row)

print("검색완료")
conn.close()