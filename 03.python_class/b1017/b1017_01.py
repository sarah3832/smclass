subject = ["국어","영어","수학","과학","역사"]
score = []

while True:
  print("1. 과목추가")
  print("0. 종료")
  choice = input("원하는 번호를 입력하세요. >> ")
  if choice == "1":
    s_input = input("과목을 추가하세요. >> ")
    subject.append(s_input)
  elif choice == "0":
    break


for i in range(len(subject)):
  score.append(int(input(f"{subject[i]}점수를 입력하세요. >> ")))

# num1 = int(input("국어점수를 입력하세요."))
# num2 = int(input("영어점수를 입력하세요."))
# num3 = int(input("수학점수를 입력하세요."))
# num4 = int(input("과학점수를 입력하세요."))
# num5 = int(input("역사점수를 입력하세요."))

sum = 0  # 합계
for i in range(len(subject)):
  print(f"{subject[i]} : ",score[i])
  sum += score[i]
print("합계 : ",sum)



# ----------------------------------



# # 함수선언
# def output(subject):
#   # 출력
#   print("[ 과목 ]")
#   print("-"*20)
#   for s in subject:
#     print(s)


# while True:
#   print("[ 과목 생성 프로그램 ]")
#   s_input = input("원하는 과목을 입력하세요. >> ")
#   print()
#   subject.append(s_input)
#   output(subject)  # 함수호출



# ----------------------------------



# a = 10
# b = 20
# c = 30

#  # 함수를 사용해서, a+b+c의 합을 a에 저장해서 출력하시오.

#  # 함수선언
# def add(a,b,c):  # 지역변수
#   return  a+b+c

# a = add(a,b,c)  # 전역변수
# print("a+b+c 합계 : ",a)



# ----------------------------------



# a = 10
# b = 20
# sum = 0

# # 함수선언
# def add(a,b):
#   return a+b  # 기본변수는 return으로 값을 돌려줘야 함.

# sum = add(a,b)  # 함수호출
# print("a+b 합계 : ",sum)



# ----------------------------------



# a = 10  # 전역변수 - 위쪽에 있어야함

# # 함수선언
# def func(a):
#   print("함수 내 a : ",a)
#   a += 50
#   return a
#   # global a  # 전역변수를 가져옴.
#   # a = 50  # 지역변수 - 함수를 종료하면 모두 제거됨.

# # 함수호출
# a = func(a)
# print("함수 밖 a : ",a)



# ----------------------------------



# subject = ["국어","영어"]

# # 함수선언
# def output(subject):
#   # 출력
#   print("[ 과목 ]")
#   print("-"*20)
#   for s in subject:
#     print(s)


# while True:
#   print("[ 과목 생성 프로그램 ]")
#   s_input = input("원하는 과목을 입력하세요. >> ")
#   print()
#   subject.append(s_input)
#   output(subject)  # 함수호출