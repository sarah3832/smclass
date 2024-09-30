# 10은 2의 배수입니다.
print("%d은 %d의 배수입니다." % (10,2))

a = 10
b = 2
print(a,b)

# 출력 자리수
print("%d" % b)
print("%5d" % b)  # 공간 5자리를 확보
print("%05d" % b) # 빈공간을 0으로 표시


# 001 010 100 3번 프린트를 사용해서 출력
# num =1
# num2 = 10
# num3 = 100
# print("%03d" % num)
# print("%03d" % num2)
# print("%.2f" % num3)
# print("%03d %03d %.2d" % (num,num2,num3))

# print("%5d" % (-10))

num = 758.12345678
num2 = 25.05
num3 = 150.15
print("%.2f" % num)

print("%013.2f" % num2)  # 소수점도 1자리 차지

print("%d" % num3)
print("%.2f" % num3)
print("%s" % num3)

print("*" * 10)


#print("숫자 : ",10) # 타입이 다른것은 + 할수없음
#print("숫자 : "+10) # 불가능
print("안녕"+"hello")
print("숫자 :",10,20,0.5,"이상")
print("-"*20)
print("-------------")
print("%5.1f" % (1234565789.123))




# 10*2=20
# print("%d * %d = %d" % (a,b,a*b))


# *** 사용표시 - %s:문자열, %c:문자1개, %f:실수, %d:정수 ***
# name = "홍길동"
# kor = 100
# eng = 100
# math = 99
# # 홍길동 총합 : 299 / 평균 : 99.666667
# print("%s 총합 : %d, 평균 : %.2f" % (name,kor+eng+math,(kor+eng+math)/3))



### print 사용 형태 ###
# print 1.쉼표, %, format, f 
# print(a,"은",b,"의 배수입니다.") # +는 ,로 입력
# print("%d은 %d의 배수입니다." % (a,b))
# print("{}은 {}의 배수입니다.".format(a,b))
# print(f"{a}은 {b}의 배수입니다.")

# # print(a+"은"+b+"의 배수입니다.") # +는 불가능