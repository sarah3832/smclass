# 학생성적 프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# studnets테이블 사용
# 시퀀스 students_seq 생성
# 번호,김유신,99,98,96 합계,평균,등수,입력일
# --------------------------------------------
import oracledb
import datetime

## db 연결 함수 선언 ##
def connects():
  user = 'ora_user'
  password = '1111'
  dsn = 'localhost:1521/xe'
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외발생 :",e)
  return conn




print("[ 학생성적 프로그램 ]")
print()
print("1. 학생성적 입력")
print("2. 학생성적 출력")
print("3. 학생성적 검색")
choice = input("원하는 번호를 입력하세요. >> ")
if choice == "1":
  print("[ 학생성적입력 ]")
  print()
  name = input("학생이름을 입력하세요. >> ")
  kor = int(input("국어점수를 입력하세요. >> "))
  eng = int(input("영어점수를 입력하세요. >> "))
  math = int(input("수학점수를 입력하세요. >> "))
  total = kor+eng+math
  avg = total/3
  rank = 0 

  st_list = [name,kor,eng,math,total,avg,rank]
  print(st_list)
  
  conn = connects()
  cursor = conn.cursor()
  sql = "insert into students values(students_seq.nextval,:1,:2,:3,:4,:5,:6,:7,sysdate)"
  cursor.execute(sql,st_list)
  conn.commit()
  cursor.close()
  print(f"{name}학생 성적이 저장되었습니다.")


elif choice == "2":
  print("[ 학생성적출력 ]")
  print()

  conn = connects()
  cursor = conn.cursor()
  sql = "select * from students"
  cursor.execute(sql)
  cursor.close()
