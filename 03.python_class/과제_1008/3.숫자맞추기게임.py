import random

r_num = random.randint(1,100)
count = 0
no = 0
for i in range(10):
  num = int(input(f"{no+1}번째 숫자를 입력하세요."))
  no += 1
  if num > r_num:
    print("입력하신 숫자가 랜덤숫자보다 큽니다.")
  elif num < r_num:
    print("입력하신 숫자가 랜덤숫자보다 작습니다.")
  else:
    print("정답! 프로그램 종료, 정답 :",num)
    count = 1
    break

if count == 0:
  print("10번 도전에 실패하셨습니다. 정답 :",r_num)