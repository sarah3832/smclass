students = []
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
chk = 0
choice = 0
count = 1
stuNo = 0
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0

while True:
  print("[ 학생성적프로그램 ]")
  print("-"*60)
  print("1. 학생성적입력")
  print("2. 학생성적출력")
  print("3. 학생성적수정")
  print("4. 학생성적검색")
  print("5. 학생성적삭제")
  print("6. 등수처리")
  print("0. 프로그램 종료")
  print("-"*60)
  choice = input("원하는 번호를 입력하세요.(0.종료)>> ")

  if choice == "1":
    print("[ 학생성적입력 ]")
    no = stuNo + 1
    name = input(f"{no}학생이름을 입력하세요.")
    kor = int(input("국어점수를 입력하세요."))
    eng = int(input("영어점수를 입력하세요."))
    math = int(input("수학점수를 입력하세요."))
    total = kor+eng+math
    avg = total/3
    rank = 0
    print(f"번호:{no},이름:{name},국어:{kor},영어:{eng},수학:{math},합계:{total},평균:{avg},등수:{rank}")
    s = [no,name,kor,eng,math,total,avg,rank]
    students.append(s)
    no += 1
    print()


  elif choice == "2":
    print(" [ 학생성적출력 ] ")
    print()
    for st in s_title:
      print(st,end="\t")
    print(); print("-"*60)
    for s in students:
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}")
    print()


  elif choice == "3":
    print(" [학생성적수정 ]")
    name = input("수정하고자 하는 학생의 이름을 입력하세요.")
    count = 0
    if s[1] == name:
      print(f"{name} 학생의 성적을 수정합니다.")
      print("[ 과목선택 ]")
      print("1. 국어점수")
      print("2. 영어점수")
      print("3. 수학점수")
      print("0. 수정안함")
      choice = input("수정할 과목을 선택하세요.>> ")
      if choice == "1":
        print(f"현재 국어점수:",s[2])
        s[2] = int(input("변경 국어점수 입력:"))
      if choice == "2":
        print(f"현재 영어점수:",s[3])
        s[3] = int(input("변경 영어점수 입력:"))
      if choice == "3":
        print(f"현재 수학점수:",s[4])
        s[4] = int(input("변경 수학점수 입력:"))
      if choice == "0":
        print("성적 수정을 취소합니다.")
        print()
        count = 1
      s[5] = s[2]+s[3]+s[4]
      s[6] = s[5]/3
      print(f"{name} 학생의 성적이 수정되었습니다.")
      print()
      for title in s_title:
        print(f"{title}\t",end="")
      print()
      print("-"*60)
      print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
      chk = 1
    if chk == 0:
      print(f"{name} 학생을 찾을 수 없습니다.")
    print()


  elif choice == "4":
    print(" [학생성적검색 ]")
    name = input("검색하고자 하는 학생을 입력하세요.>> ")
    chk = 0
    for s in students:
      if s[1] == name:
        for title in s_title:
          print(f"{title}\t",end="")
        print()
        print("-"*60)
        print(f"{s[0]}\t{s[1]}\t{s[2]}\t{s[3]}\t{s[4]}\t{s[5]}\t{s[6]:.2f}\t{s[7]}\n")
        print()
        chk = 1
      if chk == 0:
        print("검색한 이름의 학생이 없습니다.")



  elif choice == "5":
    print(" [학생성적삭제 ]")
    name = input("삭제하고자 하는 학생을 입력하세요.>> ")
    chk = 0
    for idx,s in enumerate(students):
      if s[1] == name:
        chk = 1
        choice = input(f"{name} 학생 성적을 삭제하시겠습니까?\n1.삭제 2.취소")
        if choice == 1:
          del students[idx]
          print(f"{name} 학생 성적이 삭제되었습니다.")
        else:
          print("학생 성적 삭제가 취소되었습니다.")
          break
      if chk == 0:
        print("찾고자하는 학생이 없습니다.")
        print()