# 두수를 입력받아 더하기를 출력하시오.
def plus(num1,num2):
  result = num1+num2
  return result

num1 = int(input("숫자를 입력하세요. >> "))
num2 = int(input("숫자를 입력하세요. >> "))

print(plus(num1,num2))







# def plus(n1,n2):
#   result = n1+n2
#   return result

# # 이렇게도 가능
# # def plus2(n1,n2):
# #   return n1+n2

# print(plus(1,2))
# print(plus(55,45))
# print(plus(50,50))







# # 2-50 , 3-7 , 5-50 사이의 합을 모두 더해서 출력하시오.
# def num_sum(st,end):
#   sum = 0
#   for i in range(st,end):
#     sum += i
#   return sum

# total = 0
# # print(f"2-50 까지의 합 : {num_sum(2,50):,d}")  # 천의자리 , 표시
# print("2-50 까지의 합 : {:,d}".format(num_sum(2,50)))  # 천의자리 , 표시
# print("3-7 까지의 합 : {:,d}".format(num_sum(3,7)))
# print("5-50 까지의 합 : {:,d}".format(num_sum(5,50)))

# total = num_sum(2,50)+num_sum(3,7)+num_sum(5,50)

# print("합계 : ",total)







# def num_sum(st,end):
#   sum = 0
#   for i in range(st,end):
#     sum += i
#   return sum  # 호출하는 곳으로 값을 되돌려줌

# total = 0
# num_sum(1,10)
# num_sum(1,100)
# total = num_sum(1,10)+num_sum(1,100)

# # 1-10까지 합과 1-100까지의 합의 총합을 출력하시오.
# print("합계 : ",total)

# print("프로그램 종료")






# def num_sum(st,end):  # (매개변수,매개변수)
#   sum = 0  # 지역변수
#   for i in range(st,end):
#     sum += i
#   print("합계 : ",sum)

# # 두 수를 입력받아, 그 사이의 숫자 합을 구하시오.
# # num1, num2
# # 함수를 사용해서 계산하시오.
# num1 = int(input("첫번째 숫자를 입력하세요."))
# num2 = int(input("두번째 숫자를 입력하세요."))
# num_sum(num1,num2)
# # num_sum(num1,int(input("두번째 숫자를 입력하세요.")))  # 이것도 가능


# # 1-10까지 합계를 출력하시오.
# num_sum(1,10)

# # 1-100까지 합계를 출력하시오.
# num_sum(1,100)

# # 2-50까지 합계를 출력하시오.
# num_sum(2,50)

# # 100-1000까지 합계를 출력하시오
# num_sum(100,1000)
