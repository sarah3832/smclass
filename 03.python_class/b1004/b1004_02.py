import random

# 랜덤숫자 : 1-100
# random.randint(1,100)

# 10번의 도전에서 
# 입력한 숫자가 더 크면 작은수를 입력하셔야 합니다.
# 입력한 숫자가 더 작으면 큰수를 입력하셔야 합니다. 
# 10번 도전에서 맞추지 못하면, 10번 도전에 실패했습니다. 랜덤숫자:10
# 도전에 성공 했습니다. 랜덤숫자 :10

# while
r_num = random.randint(1,100)
print("정답숫자 :",r_num)
i = 0       # 반복횟수 변수
count = 0   # 확인하는 변수

while i<10:
  num = int(input(f"{(i+1)}번째 숫자를 입력하세요."))
  if num > r_num:
    print("더 작은수를 입력하셔야 합니다.")
  elif num < r_num:
    print("더 큰수를 입력하셔야 합니다.")
  else:
    print(f"도전에 성공 했습니다. 랜덤숫자: {r_num}")
    count = 1
    break
  i += 1

if i == 10:
  print(f"10번 도전에 실패했습니다. 랜덤숫자: {r_num}")


# # for
# r_num = random.randint(1,100)
# cnt = 0
# i = 0

# for n in range(10):
#   num = int(input("숫자를 입력하세요."))
#   if num > r_num:
#     print(i+1,"번째 도전!더 작은수를 입력하세요.")
#   elif num < r_num:
#     print(i+1,"번째 도전!더 큰수를 입력하세요.")
#   else:
#     print("도전에 성공! 랜덤숫자 : ",r_num)
#     cnt = 1
#     break

# if cnt == 0:
#   print("도전에 실패! 랜덤숫자 : ",r_num) 

