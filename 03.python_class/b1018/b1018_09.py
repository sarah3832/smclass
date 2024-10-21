# Student 클래스 생성 후
# 데이터를 직접 입력을 받아, 클래스 선언 후 저장
# 번호-자동부여,이름,국어,영어,수학,합계,평균,등수
# 클래스 전체 출력
# 클래스 수정

# [ 학생성적 프로그램 ]
# 1. 학생성적 입력
# 2. 학생성적 출력
# 3. 학생성적 수정

# ----------------------------------------
class Student:
  count = 0
  students = []
  @classmethod
  def stu_print(cls):
    for s in cls.students:
      print(str(s))

  def __init__(self,name,kor,eng,math):
    Student.count += 1
    self.no = Student.count
    self.name = name
    self.kor = kor
    self.eng = eng
    self.math = math
    self.total = kor+eng+math
    self.avg = (kor+eng+math)/3
    self.rank = 0
    Student.students.append(self)
    
  def __str__(self):
    return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}\t"
  
  def print(self):
    return {"no":self.no,"name":self.name,"kor":self.kor,"eng":self.eng,"math":self.math,"total":self.total,"avg":self.avg,"rank":self.rank}
  

# ----------------------------------------

s_t = ['no','name','kor','eng','math','total','avg','rank']
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

while True:
  print("[ 학생성적 프로그램 ]")
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 수정")
  choice = int(input("원하는 번호를 입력하세요. >> "))
  if choice == 1:
    print("[ 학생성적 입력 ]")
    name = input("학생 이름을 입력하세요. >> ")
    score = []
    for i in range(2,5):
      score.append(int(input(f"{s_title[i]}점수를 입력하세요. >> ")))
    Student(name,*score)

    for s in Student.students:
      print(s)

  elif choice == 2:
    print("[ 학생성적 출력 ]")
