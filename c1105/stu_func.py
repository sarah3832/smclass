import oracledb

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']

# db연결 함수선언
def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"
  try: conn = oracledb.connect(user=user,password=password,dsn=dsn)
  except Exception as e: print("예외처리 : ",e)
  return conn

#### 0. 메인화면 출력 함수 선언
def main_print():
  print()
  print("  [  학생 성적 프로그램  ]")
  print("1. 학생 성적 입력")
  print("2. 학생 성적 출력")
  print("3. 학생 성적 검색")
  print("4. 학생 성적 정렬")
  print("5. 학생 등수 처리")
  print("0. 프로그램 종료")
  choice = input("원하는 번호 입력 >> ")
  print()
  return choice

### 1.학생성적입력 함수선언
def stu_insert():
  conn = connects()
  cursor = conn.cursor()
  print("[ 학생성적 입력 ]")
  # sql = "select students_seq.currval from dual"
  # cursor.execute(sql)
  # row = cursor.fetchone()
  cursor.close()
    # no = row[0]
  name = input("번째 학생이름을 입력하세요. >> ")
  kor = int(input("국어점수를 입력하세요. >> "))
  eng = int(input("영어점수를 입력하세요. >> "))
  math = int(input("수학점수를 입력하세요. >> "))
  total = kor+eng+math
  avg = total/3
  s_list = [name,kor,eng,math,total,avg]

  # insert, update, delete 경우 conn.commit() 하셔야 반영됨.
  conn = connects()
  cursor = conn.cursor()
  sql = "insert into students values(students_seq.nextval,:1,:2,:3,:4,::5,:6,0,sysdate"
  cursor.execute(sql,s_list)
  conn.commit()
  conn.close()
  print("학생성적이 저장되었습니다.")
  print() 

### 2.학생성적출력 함수선언
def stu_output():
  sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
  print("[ 학생성적 출력 ]")
  ###
  for idx,s in enumerate(s_title):
    if idx == 1:
      print(f"{s:12}",end="\t")
      continue
    print(s,end="\t")
  print()
  print("-"*80)

  # db연결
  conn = connects()
  cursor = conn.cursor()
  cursor.execute(sql)
  rows = cursor.fetchall()
  print(f"[ 개수 : {len(rows)} ]")

  if len(rows)<1:
    print("데이터가 없습니다.")
    return

  for row in rows:
    for idx,r in enumerate(row):
      if idx == 1:
        print(f"{r:12}",end="\t")
        continue
      print(r,end="\t")
    print()
  print()
  print("데이터 출력완료!")

### 3.학생성적검색 함수선언
def stu_search():
  print("[ 학생성적 검색 ]")  # a포함되어 있는 학생을 검색
  print("1. 이름으로 검색")
  print("2. 합계순 검색")
  choice = input("원하는 번호를 입력하세요. >> ")

  if choice == "1":
    print("[ 이름으로 검색 ]")
    search = input("찾고자하는 이름을 입력하세요. >> ")
    search = '%'+search+'%'
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students where name like :search"

      ##### 출력부분 #####
    # db연결
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql,search=search)
    rows = cursor.fetchall()
    print(f"[ 개수 : {len(rows)} ]")
    for idx,s in enumerate(s_title):
      if idx == 1:
        print(f"{s:12}",end="\t")
        continue
      print(s,end="\t")
    print()
    print("-"*80)
    if len(rows)<1:
      print("데이터가 없습니다.")
      return
    for row in rows:
      for idx,r in enumerate(row):
        if idx == 1:
          print(f"{r:12}",end="\t")
          continue
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료!")

### 4.학생성적정렬 함수선언
def stu_align():
  print("[ 학생성적 정렬 ]")
  print("1. 이름 순차정렬")
  print("2. 이름 역순정렬")
  print("3. 합계 순차정렬")
  print("4. 합계 역순정렬")
  choice = input("원하는 번호를 입력하세요. >> ")
  
  if choice == "1":
    print("[ 이름순차정렬 ]")
    # db연결
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by name"
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for idx,s in enumerate(s_title):
      if idx == 1:
        print(f"{s:12}",end="\t")
        continue
      print(s,end="\t")
    print()
    print("-"*80)
    for row in rows:
      for idx,r in enumerate(row):
        if idx == 1:
          print(f"{r:12}",end="\t")
          continue
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료!")

  if choice == "2":
    print("[ 이름역순정렬 ]")
    # db연결
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by name desc"
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for idx,s in enumerate(s_title):
      if idx == 1:
        print(f"{s:12}",end="\t")
        continue
      print(s,end="\t")
    print()
    print("-"*80)
    for row in rows:
      for idx,r in enumerate(row):
        if idx == 1:
          print(f"{r:12}",end="\t")
          continue
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료!")

  if choice == "3":
    print("[ 합계순차정렬 ]")
    # db연결
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by total desc"
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for idx,s in enumerate(s_title):
      if idx == 1:
        print(f"{s:12}",end="\t")
        continue
      print(s,end="\t")
    print()
    print("-"*80)
    for row in rows:
      for idx,r in enumerate(row):
        if idx == 1:
          print(f"{r:12}",end="\t")
          continue
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료!")

  if choice == "4":
    print("[ 합계역순정렬 ]")
    # db연결
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students order by total"
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for idx,s in enumerate(s_title):
      if idx == 1:
        print(f"{s:12}",end="\t")
        continue
      print(s,end="\t")
    print()
    print("-"*80)
    for row in rows:
      for idx,r in enumerate(row):
        if idx == 1:
          print(f"{r:12}",end="\t")
          continue
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료!")
