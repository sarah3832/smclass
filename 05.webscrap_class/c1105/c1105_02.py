# 2. 함수선언 - 가변매개변수
def func(*num):  # 튜플타입
  print(num)  
  print(len(num))  
  
# 함수호출 - 개수를 맞추지 않아도 출력가능
func(10)
func(10,20)
func(10,20,30)

#-------------------------------

# 1. 함수선언 - 기본매개변수
# def func(num1,num2):
#   print(num1)
#   print(num2)

# 함수호출
# func(10,20)

# 함수의 매개변수 개수를 정확히 맞춰야 에러가 안남
# func(10,20,30)  # 에러
# func(10)  # 에러