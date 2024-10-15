# students 리스트 타입
students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수

# ---------------- 함수선언 ------------------

# 학생성적출력 함수선언
def stu_output(s_title,students):
  print("[ 학생성적 출력 ]")
  print()

  # 상단 출력
  for st in s_title:
    print(st,end="\t")
  print(); print("-"*60)
  
  # 학생성적 출력
  for s in students:
    print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
  print()
# -------------------------------------------


# 학생성적수정 함수선언
def stu_update(s_title,students):
  print("[ 학생성적수정 ]")
  name = input("찾고자 하는 학생의 이름을 입력하세요.")
  chk = 0
  for s in students:
    if s[1] == name:
      # 학생성적 수정
      print(f"{name} 학생을 찾았습니다.")
      print()
      print("[ 수정 과목 선택 ]")
      print("1. 국어점수")
      print("2. 영어점수")
      print("3. 수학점수")
      choice = input("원하는 번호를 입력하세요.>> ")
      if choice == "1":
        print("이전 국어점수 : {}".format(s[2]))
        s[2] = int(input("변경 국어점수 : "))
      elif choice == "2":
        print("이전 영어점수 : {}".format(s[3]))
        s[3] = int(input("변경 영어점수 : "))
      elif choice == "3":
        print("이전 수학점수 : {}".format(s[4]))
        s[4] = int(input("변경 수학점수 : "))
      s[5] = s[2]+s[3]+s[4]  # 합계
      s[6] = s[5]/3          # 평균
      print(f"{name} 학생 성적이 수정되었습니다.")
      print()
      # 학생출력
      # 상단타이틀 출력
      for title in s_title:
        print(f"{title}\t",end="")
      print()
      print("-"*60)
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
      print()
      chk = 1
  # 모든 학생 비교가 끝난 후, chk 확인
  if chk == 0:
    print(f"{name} 학생이 없습니다. 다시 입력하세요.")
  print()




# -------------------------------------------



choice = input("원하는 번호를 선택하세요.(3.학생성적수정) >> ")

if choice == "3":
  print("[ 학생성적수정 ]")
  name = input("찾고자 하는 학생의 이름을 입력하세요.")

# 전체학생과 비교
  flag = 0
  for s in students:
    if name == s['name']:
      print(f"{name} 학생을 찾았습니다.")
      print("[ 수정 과목 선택 ]")
      print("1. 국어점수")
      print("2. 영어점수")
      print("3. 수학점수")
      choice = input("원하는 번호를 입력하세요.>> ")
      if choice == "1":
        print("이전 국어점수 : {}".format(s['kor']))
        s['kor'] = int(input("변경 국어점수 : "))
      elif choice == "2":
        print("이전 영어점수 : {}".format(s['eng']))
        s['eng'] = int(input("변경 영어점수 : "))
      elif choice == "3":
        print("이전 수학점수 : {}".format(s['math']))
        s['math'] = int(input("변경 수학점수 : "))

      s['total'] = s['kor']+s["eng"]+s["math"]
      s['avg'] = s["total"]/3

      print(f"{name} 학생 성적이 수정되었습니다.")

      # 수정된 학생성적을 출력 - 학생성적출력함수 재사용
      stu_output(s_title,[s])

      flag = 1

    # 학생이 검색되지 않았을때
  if flag == 0:
    print(f"{name} 학생이 없습니다. 다시 입력하세요.")
    print()


  elif choice == "3":
    stu_update(s_title,students)