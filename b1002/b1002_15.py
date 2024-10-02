# 숫자맞추기
import random

# for
r_num = random.randint(1,50)
count = 0
for i in range(10):
  num = int(input("숫자입력"))
  if num > r_num:
    print("입력한 숫자가 랜덤숫자보다 큽니다.")
  elif num < r_num:
    print("입력한 숫자가 랜덤숫자보다 작습니다.")
  else:
    print("정답!",num)
    count = 1
    break

if count == 0:
  print("10번 도전 실패! 정답번호 :",r_num)  


# while