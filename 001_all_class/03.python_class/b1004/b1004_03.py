# 0부터 1씩 증가하면서, 10번 실행
for i in range(10):
  print(i)
print("-"*50)

# 5부터 9까지(10이전까지) 5번 실행
for j in range(5,10):
  print(j)

# 구구단 1,3,5,7,9 출력하시오.
for i in range(1,10,2):      # (시작값, 끝값+1, 증가값) - 1씩증가는 1생략가능
  for j in range(2,10):
    print(f"{i} x {j} = {i*j}")


print("-"*50)
a_list = [1,2,3,4,5]
for k in a_list:
  print(k)

# 파이썬 - 문자열(str), 정수형(int), 실수형(float), 논리형(bool)
# 리스트 타입 - []
print("-"*50)
b_list = [3,5,9,10,20,3,3,10,5,20]
for n in b_list:
  print(n)


# 딕셔너리 타입 - {} : json타입과 모양이 같음 / 키,값(key,value) / 세로,가로 나열방법 상관없음
dic = {
  "번호":1,  # "key":value
  "이름":"홍길동",
  "국어":100,
  "영어":100,
  "수학":99
}
print(dic["번호"])
print(dic["이름"])

for d in dic:  # dic에서 key값을 d에 넣어줌 / for문에 딕셔너리 가능
  # print(d)  # key값이 출력이 됨
  print(dic[d])  # key값의 value값이 출력이 됨


# 리스트 길이 : len()
print(len(b_list))

# 리스트 안에 해당되는 숫자가 몇개인지 확인 - count(찾는 숫자입력)
print(b_list.count(5))

# 리스트 추가 - append / insert / extend([2,3]) : 리스트를 추가할때
# 리스트 삭제 - del / remove / clear(모두삭제)