import random

# 1-100까지의 랜덤숫자를 생성
# 입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다.
# 입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다.
# 10번 도전하도록 하시오.
# 정답입니다. 프로그램종료 하시오. break


# *** while 활용 ***
# 랜덤숫자는 while 밖에 있어야함
# i = 0  # 초기값
# r_num = random.randint(1,100)  # while 돌때마다 랜덤숫자 같이 변경
# count = 0
# while i<10:  # 조건식
#  num = int(input("숫자를 입력하세요."))
# # 비교구문
#  if num > r_num:
#     print("입력한 숫자가 큽니다.")
#  elif num < r_num:
#     print("입력한 숫자가 작습니다.")
#  else:
#     print("정답입니다. 프로그램 종료",num)
#     break
#  i += 1  # 증감식

# # 10번 도전해서 실패 할 경우
# if count == 0:
#   print("10번 도전에 실패하셨습니다. 정답번호: ",r_num)


# *** for 활용 ***
r_num = random.randint(1,100)
count = 0
for i in range(10):
  num = int(input("숫자를 입력하세요."))
# 비교구문
  if num > r_num:
    print("입력한 숫자가 큽니다.")
  elif num < r_num:
    print("입력한 숫자가 작습니다.")
  else:
    print("정답입니다. 프로그램 종료",num)
    count = 1
    break

  # 10번 도전해서 실패 할 경우
if count == 0:
  print("10번 도전에 실패하셨습니다. 정답번호: ",r_num)




 

