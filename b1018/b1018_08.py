# ** 변수 3종류 **
# 지역 변수 : 함수내에 선언된 변수, 함수가 종료가되면 사라짐.
# 인스턴스 변수 : 객체 선언할때 만들어짐, 각각의 객체마다 변수가 생성됨.
# (사용방법) - 참조변수명.변수명 
# 클래스 변수 : 객체가 선안되지 않아도 만들어짐, 모든 객체가 공통으로 사용.
# (사용방법) - 클래스명.변수명 

# ** 함수 2종류 **
# 인스턴스 함수 : 객체 선언할때 만들어짐, 각각의 객체마다 함수가 생성됨
# (사용방법) - 참조변수명.함수명
# 클래스 함수 : 객체가 선언되지 않아도 만들어짐, 모든 객체가 공통으로 사용
# (사용방법) - 클래스명.함수명
# @classmethod : 클래스 함수 표시

# 객체선언 한 참조변수를 출력하면 -> 주소값이 출력됨.
# - 참조변수를 출력해서 원하는 데이터를 출력하려면, __str__ 함수를 사용
# 리턴값 : 문자열이여야 함.

# ----------------------------------------------

# 1. 학생성적입력
# 이름,국어,영어,수학 -> 번호,국어,영어,수학,합계,평균,등수
# 클래스 1개가 생성이 되고
# 클래스의 참조변수를 (__str__) 출력을 해보세요.
# ----------------------------------------------

# 클래스 생성
class Student:

  count = 1
  students = []

  @classmethod
  def stu_print(cls):
    for s in cls.students:
      print(str(s))

  # kor = 100  # 클래스 변수 : 클래스명.변수명
  def __init__(self,name,kor,eng,math):
    self.no = Student.count  # 클래스 변수 : 클래스명.변수명
    self.name = name         # 인스턴스 변수 : 참조변수명.변수명
    self.kor = kor
    self.eng = eng
    self.math = math
    Student.count += 1
    Student.students.append(self)

  def __str__(self):
    return f'{self.no},{self.name},{self.kor},{self.eng},{self.math}'  #  리턴값 : 문자열이여야 함.

  # no getter를 사용하지 않으면 접근불가
  def get_no(self):
    return self.no
  def set_no(self,no):
    if no < 0: raise "0 이하는 입력을 할 수 없습니다."
    self.no = no


s1 = Student("홍길동",100,100,100)
print(s1)
s2 = Student("유관순",100,100,90)
print(s2)
s3 = Student("이순신",100,100,80)
print(s3)
s4 = Student("강감찬",100,100,70)
print(s4)

print("-"*50)
# 클래스 __str__ 
# Student.stu_print()
# Student.students 리스트
for s in Student.students:
  print(s)


# print("최초 :",Student.kor)

# s1 = Student(10)
# print(s1.no)
# Student.kor = 50

# s2 = Student(20)
# print(s2.no)

# print("최종 :",Student.kor)





  # def __init__(self,name,kor,eng,math):
  #   Student.count += 1
  #   self.no = Student.count
  #   self.name = name
  #   self.kor = kor
  #   self.eng = eng
  #   self.math = math
  #   self.total = kor+eng+math
  #   self.avg = (kor+eng+math)/3
  #   self.rank = 0
  #   Student.students.append(self)

# --------------------------
  # s1 = Student()  # 객체선언


  # students = []
  # count = 0


  # def __str__(self):
  #   return f"{self.no}\t{self.name}\t{self.kor}\t{self.eng}\t{self.math}\t{self.total}\t{self.avg}\t{self.rank}\t"


# s_t = ['no','name','kor','eng','math','total','avg','rank']
# s_title = ['번호','이름','국어','영어','수학','합계','평균','등수']

# while True:
#   print("[ 학생성적 입력 ]")
#   name = input("이름을 입력하세요. >> ")
#   score = []
#   for i in range(2,5):
#     score.append(int(input(f"{s_title[i]}점수를 입력하세요. >> ")))
