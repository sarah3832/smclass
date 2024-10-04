# 두 수를 입력받아, 두 수까지 합계를 구하시오.
# 큰수, 작은수를 입력해도 합계를 구하시오.
# 예) 3,8 -> 3+4+5+6+7+8

# 3. if문을 사용
num1 = int(input("첫번째 숫자"))
num2 = int(input("두번째 숫자"))
# num3 = 0  # 다른 언어들은 변수를 하나 줘야함

if num1>num2:  
  num1,num2 = num2,num1  # 이 형태는 파이썬만 가능 : 두개 변수 바꿀수있음
  # num3 = num1
  # num1 = num2
  # num2 = num3   # 다른 언어들 방법

sum = 0
for i in range(num1,num2+1):
  if num1 >= num2 or num1 <= num2:
   sum += i
print("합계 : ",sum)


# # 2. min,max 함수 사용
# num1 = int(input("첫번째 숫자"))
# num2 = int(input("두번째 숫자"))

# # min_num = min(num1,num2); max_num = max(num1,num2)  # ; 으로 넣어야함

# sum = 0
# for i in range(min(num1,num2),max(num1,num2)+1):  # min,max 여기 넣으면 위에 안적어도됨
#   if num1 >= num2 or num1 <= num2:
#    sum += i
# print("합계 : ",sum)


# # 1. if문을 사용
# num1 = int(input("첫번째 숫자"))
# num2 = int(input("두번째 숫자"))
# num3 = 0
# min_num = num1; max_num = num2  # ; 으로 넣어야함
# if num1>num2:
  #  num3 = num1
  #  num1 = num2
  #  num2 = num3

# sum = 0
# for i in range(num1,num2+1):
#   if num1 >= num2 or num1 <= num2:
#    sum += i
# print("합계 : ",sum)




# # 1,3,5,7,9 ...99 홀수 합계를 구하시오.

# sum = 0
# for i in range(1,100+1,2):
#     sum += i 
# print("합계 : ",sum)

# sum = 0
# for i in range(1,100+1):
#   if i%2 !=0:
#     sum += i 
# print("합계 : ",sum)



# # 1-100까지 숫자의 합
# sum = 0
# for i in range(1,100+1):
#   sum += i
# print("합계 : ",sum)




# # 0: 안녕하세요.
# # 1: 안녕하세요.
# # 2: 안녕하세요.
# for i in range(3):
#   print(f"{i}: 안녕하세요.")

# for _ in range(3):  # _ : 아무 변수도 안받음
#   print("안녕하세요.")





# 1 - 1번출력, 2 - 2번출력, 3 - 3번출력

# for i in [1,2,3]:
#   for j in range(i):
#     print("안녕하세요.")
#   print("-"*30)


# for i in [1,2,3]: # 3번출력
#   print("안녕하세요.\n"*i,end="")  # end="" <- \n 없애기
#   print("-"*30)




# for i in range(5,0,-1):  # -1씩 감소
#   print("*"*i)  # 5,4,3,2,1
# # *****
# # ****
# # ***
# # **
# # *


# for i in range(1,6):
#   print("*"*i)  # 1,2,3,4,5
# # *
# # **
# # ***
# # ****
# # *****

# # for문을 사용해서
# for i in range(0,6):
#   for j in range(5):
#    print("*"*5)
# *
# **
# ***
# ****
# *****




# range(시작값, 끝값+1, 증가값)
# # 구구단 1,3,5,7,9 출력하시오.
# for i in range(1,10,2):      # (시작값, 끝값+1, 증가값) - 1씩증가는 1생략가능
#   for j in range(2,10):
#     print(f"{i} x {j} = {i*j}")

# # 구구단 1,3,5,7,9 출력하시오.
# for i in range(1,10):
#   if i%2 != 0:   # if문 사용해서 홀수만 출력
#    print(f"[ {i} 단 ]")
#    for j in range(2,10):
#     for j in range(2,10):
#    print("-"*20)  



# # 구구단을 출력하시오. # for문 두개사용
# for i in range(2,10):  
#   print(f"[ {i} 단 ]")  # 1번 반복
#   for j in range(1,10):  # 9번 반복
#     print(f"{i} x {j} = {i*j}")  # 9번 반복
#   print("-"*20)  # 1번 반복



# # 1,3,5,7,9 까지 출력하시오.
# for i in range(10):  # if문 사용해서 홀수만 출력
#   if i%2 != 0:
#     print(i)



# # 1-10 까지 for문을 사용해서 출력하시오.
# for i in range(1,11):  # 11이전까지 = (1,10+1)
#   print(i)


# 파이썬 튜터
# a = [1,2,3,4,5,]
# b = [*a]
# c = a

# c = 100
# d = c

# d = 1
# b[1] = 100

# print(a)
# print(c)