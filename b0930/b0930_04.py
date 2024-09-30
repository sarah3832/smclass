# *** bool(불형), int(정수), float(실수), str(문자형) ***

# name, kor, eng, math, total, avg 출력
# input 으로 입력을 받아
# 홍길동, 100, 100, 99, 합계, 평균(소수점 둘째자리)을 1줄에 출력하시오.
# format, f함수 사용

name = input("홍길동")
kor = input("100")
eng = input("100")
math = input("99")
print(type(kor))
total = int(kor)+int(eng)+int(math)  # 문자열에서 정수형으로 타입변경
avg = total/3
print("{},{},{},{},{},{:.2f}".format(name,kor,eng,math,total,avg))
print(f"{name},{kor},{eng},{math},{total},{avg:.2f}")




# a = '100'
# b = "200"
# print(type(a))
# print(type(b))

# print(a+b)  # 문자연결연산자 100200
# print(int(a)+int(b))  # 타입변경

# name = "홍길동"
# # print(int(name))  # 문자를 숫자로는 변경 불가능, 문자숫자는 가능
# c = "3.14"
# print(int(float(c)))  # 실수형으로 변경 후, 정수형으로 변경
# # print(int(c))  # 문자실수형은 정수로 바로 변경 불가능
# print(str(c))  # 실수형을 문자열로 변경

# d = "True"
# print(bool(d))  # 문자불형을 불형으로 변경

# 타입 변경 - bool, str, float, int



# srt : "",'' 둘다 상관없음
# name = "홍길동"
# print(type(name))
# level = '3레벨'
# print(type(level))

# n = 3.14
# print(type(n))

# num = 100
# print(type(num))

# a_bool = True  # True, False 대문자로 넣어야 함
# print(type(a_bool))


# var1 = 100
# var2 = var1
# var3 = var2
# var4 = var3 
# print(var4)

# v4 = v3 = v2 = v1 = 10
# print(v4)