a = [1,2,3,4,5]
# 얕은 복사 = 주소값만 복사됨
b = a
print(a)  # [1,2,3,4,5]

b[0] = 100  
print(a)


#### 데이터 값이 1개일때 ####
# num = 10     # num 메모리 주소값과
# num2 = num   # num2 메모리 주소값이 다름
# num2 = 20    # num2 변경해도 num의 값은 변경이 안됨

# print(num)  #10
# print(num2) #20


