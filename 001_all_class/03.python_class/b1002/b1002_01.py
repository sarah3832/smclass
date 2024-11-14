# 문자열

# 문자열숫자
a = "123"
print(type(a))        # str
print(type(int(a)))   # int
print(type(float(a))) # float

b = "12.3"
# print(type(int(b)))   # 에러 - 소수점이 있는 문자열숫자는 flaot 변경해야 함
print(type(float(b)))   # float

# 문자열 연결연산자 +
s1 = "안녕"
s2 = "안녕하세요."
print(s1+s2)
print(a+b)  # 문자열 연결연산자 +
# print(a*b)  # 에러 - 문자열은 -.*,/ 불가능

# 문자열 *2 
print("안녕"*10)  # 문자열 반복 연산자 
print("-."*30)

# 문자열 슬라이싱
str1 = "안녕하세요.반갑습니다."  # 문자열 자체를 리스트 형태로 봄
print(str1[0])    # 해당번호 넣으면 해당되는 문자출력
print(str1[6])
print(str1[2:5])  # 해당범위 출력 : [위치:위치 한칸 뒤]
print(str1[:5])   # [처음:숫자 앞 까지]
print(str1[2:])   # [위치:끝까지]
print(str1[1:10:2])  # [위치:숫자 앞까지:step2]
print(str1[1:10:3])  # [위치:숫자 앞까지:step3]
print(str1[::-1])  # [처음:끝까지:역순으로]  ㄴ

# [] - 배열 : 배열은 한번 범위가 정해지면 수정이 불가 (c,자바)
# [] - 리스트 : 범위 상관없음 

c = 12.3
print(type(int(c)))   # 실수는 int타입으로 변경가능
print(int(c))





# input_str = input("글자를 입력하세요.")

# # 문자가 입력되지 않았을때
# if input_str != "":  # 빈공백이 아니냐? (!="") / != : not 
#   print("글자를 입력하셔야 합니다.")
# else:
#  print("입력문자 : ",input_str)
#  print("프로그램이 종료됩니다.")


# and = 둘 다 참이어야 참 (a>100)and(a<200)
# or  = 둘 중 하나만 참이어야 참 (a==100)or(a==200)
# not = 참이면 거짓, 거짓이면 참 not(a<100)


