studendts = []
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']
choice = 0
chk = 0
stuNo = 0
count = 1
stuNo = len(studendts)
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0

while True:
  print("[ 학생성적프로그램 ]")
  print("*"*60)
  print("1) 학생성적입력 ")
  print("2) 학생성적출력 ")
  print("3) 학생성적수정 ")
  print("4) 학생성적검색 ")
  print("5) 학생성적삭제 ")
  print("6) 등수처리 ")
  print("7) 학생성적정렬 ")
  print("0) 프로그램 종료 ")
  print("*"*60)
  choice = input("원하는 번호를 입력하세요.(종료:0) >> ")

  if choice == "1":
    while True:
      print("[ 학생성적입력 ]")
      no = stuNo + 1
      name = input(f"{no}번째 학생이름을 입력하세요.(0:이전화면) >> ")
      if name == "0":
        print("이전화면으로 돌아갑니다.")
        print()
        break
      kor = int(input("국어점수를 입력하세요."))
      eng = int(input("영어점수를 입력하세요."))
      math = int(input("수학점수를 입력하세요."))
      total = kor+eng+math
      avg = total/3
      rank = 0
      ss = {"no":no,"name":name,"kor":kor,"eng":eng,"math":math,
            "total":total,"avg":avg,"rank":rank}
      studendts.append(ss)
      stuNo += 1
      print(f"{name} 학생의 성적이 저장되었습니다!")
      print()


  elif choice == "2":
    print("[ 학생성적출력 ]")
    print()
    for st in s_title:
      print(st,end="\t")
    print(); print("-"*60)
    for s in studendts:
      print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
    print()
    

  elif choice == "3":
    print("[ 학생성적수정 ]")
    name = input("수정하고자 하는 학생의 이름을 입력하세요.")
    chk = 0
    for s in studendts:
      if s['name'] == name:
        print(f"{name} 학생의 성적을 수정합니다.")
        print()
        print("[ 수정과목선택 ]")
        print("1. 국어점수")
        print("2. 영어점수")
        print("3. 수학점수")
        print("0. 수정안함")
        choice = input("원하는 번호를 입력하세요. >> ")
        if choice == "1":
          print(f"이전 국어점수 : {s['kor']}")
          s['kor'] = int(input("변경 국어점수 : "))
        elif choice == "2":
          print(f"이전 영어점수 : {s['eng']}")
          s['eng'] = int(input("변경 영어점수 : "))
        elif choice == "3":
          print(f"이전 수학점수 : {s['math']}")
          s['math'] = int(input("변경 수학점수 : "))
        elif choice == "0":
          print("성적수정을 취소합니다.")
          print()
          chk = 1

        if choice != "0":
          s['total'] = s['kor']+s['eng']+s['math']
          s['avg'] = s['total']/3
          print(f"{name} 학생 성적이 수정되었습니다.")
          chk = 1

      if chk == 0:
        print(f"{name} 학생이 없습니다. 다시 입력하세요.")
      print()


  elif choice == "4":
    print("[ 학생성적검색 ]")
    name = input("찾고자하는 학생의 이름을 입력하세요. >> ")
    chk = 0
    for s in studendts:
      if s['name'] == name:
        print(f"{name} 학생을 찾았습니다.")
        for st in s_title:
          print(st,end="\t")
        print(); print("-"*60)
        print(f"{s['no']}\t{s['name']}\t{s['kor']}\t{s['eng']}\t{s['math']}\t{s['total']}\t{s['avg']:.2f}\t{s['rank']}")
        print()
        chk = 1
        break
      if chk == 0:
        print(f"{name} 학생이 없습니다. 다시 입력하세요.")
        print()


  elif choice == "5":
    print("[ 학생성적삭제 ]")
    name = input("삭제하고자 하는 학생의 이름을 입력하세요. >> ")
    chk = 0
    for idx,s in enumerate(studendts):
      if s['name'] == name:
        chk = 1
        choice = input(f"{name} 학생의 성적을 삭제하시겠습니까? (삭제시 복구불가)\n1.삭제 2.취소")
        if choice == "1":
          del studendts[idx]
          print(f"{name} 학생의 성적이 삭제되었습니다.")
        else:
          print("삭제가 취소되었습니다.")
          break
      if chk == 0:
        print(f"{name} 학생이 없습니다. 다시 입력하세요.")


  elif choice == "6":
    print("[ 등수처리 ]")
    for s in studendts:
      count = 1
      for st in studendts:
        if s['total'] < st['total']:
          count += 1
      s['rank'] = count
    print("등수처리가 완료되었습니다.")
    print()


  elif choice == "7":
    while True:
      print("[ 학생성적정렬 ]")
      print("1. 이름 순차정렬")
      print("2. 이름 역순정렬")
      print("3. 합계 순차정렬")
      print("4. 합계 역순정렬")
      print("5. 번호 순차정렬")
      print("0. 이전페이지")
      print("-"*60)
      choice = input("원하는 번호를 입력하세요.")
      print()

      if choice == "1":
        studendts.sort(key=lambda x:x['name'])
        print("정렬이 완료되었습니다.")
        print()
      elif choice == "2":
        studendts.sort(key=lambda x:x['name'],reverse=True)
        print("정렬이 완료되었습니다.")
        print()
      elif choice == "3":
        studendts.sort(key=lambda x:x['total'])
        print("정렬이 완료되었습니다.")
        print()
      elif choice == "4":
        studendts.sort(key=lambda x:x['total'],reverse=True)
        print("정렬이 완료되었습니다.")
        print()
      elif choice == "5":
        studendts.sort(key=lambda x:x['no'])
        print("정렬이 완료되었습니다.")
        print()
        
      elif choice == "0":
        print("이전페이지로 이동합니다.")
        break


  elif choice == "0":
    print("[ 학생성적프로그램 종료 ]")
    print("프로그램을 종료합니다.")
    break
        