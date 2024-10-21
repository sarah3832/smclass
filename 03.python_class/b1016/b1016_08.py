# sm shop
import datetime

# member 파일 읽어와서 member딕셔너리 저장
member = []
m_keys = ['id','pw','name','nicName','address','money']

f = open('member.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line: break
  m = line.strip().split(",")
  m[5] = int(m[5])
  member.append(dict(zip(m_keys,m)))
  # print(member)


# cart 파일 읽어와서 cart 저장
cartNo = 0
cart = []
c_keys = ["cno","id","name","pCode","pName","price","date"]

f = open('cart.txt','r',encoding='utf-8')
while True:
  line = f.readline()
  if not line:break
  c = line.strip().split(",")
  c[0] = int(c[0])
  c[5] = int(c[5])
  cart.append(dict(zip(c_keys,c)))
f.close()










product = [
  {"pno":1,"pCode":"t001","pName":"삼성TV","price":2000000,"color":"black"},
  {"pno":2,"pCode":"g001","pName":"LG냉장고","price":3000000,"color":"white"},
  {"pno":3,"pCode":"h001","pName":"하만카돈스피커","price":500000,"color":"gray"},
  {"pno":4,"pCode":"w001","pName":"세탁기","price":1000000,"color":"yellow"}
]

session_info = {}
p_title = ["번호","아이디","이름","코드","상품명","가격","구매일자"]



while True:
  print("[ 로그인 화면 ]")
  id_input = input("아이디를 입력하세요. >> ")
  pw_input = input("비밀번호를 입력하세요. >> ")
  flag = 0
  for m in member:
    if id_input == m['id'] and pw_input == m['pw']:
      print("SM SHOP에 오신것을 환영합니다!")
      session_info = m
      flag = 1
      break
  
  if flag == 0:
    print("아이디 또는 비밀번호가 일치하지 않습니다.")
  else:
    break



while True:
  print("       [ SM SHOP ]")
  print()
  print(f"*** 닉네임 : {session_info['nicName']} 님 ***")
  print(f"*** 금액 : {session_info['money']:,} 원 ***")
  print()
  print("1. 삼성TV - 2,000,000")
  print("2. LG냉장고 - 3,000,000")
  print("3. 하만카돈스피커 - 500,000")
  print("4. 세탁기 - 1,000,000")
  print()
  choice = int(input("원하는 번호를 입력하세요. >> "))
  