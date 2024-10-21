# 숫자맞추기
import random

# # for
# r_num = random.randint(1,50)
# count = 0
# for i in range(10):
#   num = int(input("숫자입력"))
#   if num > r_num:
#     print("입력한 숫자가 랜덤숫자보다 큽니다.")
#   elif num < r_num:
#     print("입력한 숫자가 랜덤숫자보다 작습니다.")
#   else:
#     print("정답!",num)
#     count = 1
#     break

# if count == 0:
#   print("10번 도전 실패! 정답번호 :",r_num)  


# 1-100까지의 랜덤숫자를 생성
# 입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다.
# 입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다.
# 10번 도전하도록 하시오.
# 정답입니다. 프로그램종료 하시오. break

# while

# r_num = random.randint(1,100)
# i = 0

# while i<10:
#   num = int(input("숫자입력"))
#   if num > r_num:
#     print("입력숫자가 랜덤숫자보다 큽니다.")
#     i += 1
#   elif num < r_num:
#     print("입력숫자가 랜덤숫자보다 작습니다.")
#     i += 1
#   else:
#     print("정답, 프로그램 종료")
#     break

# if i == 10:
#   print("탈락")



# 1-100까지의 랜덤숫자를 생성
# 입력한 숫자가 랜덤숫자보다 크면 입력한 숫자가 큽니다.
# 입력한 숫자가 랜덤숫자보다 작으면 입력한 숫자가 작습니다.
# 10번 도전하도록 하시오.
# 정답입니다. 프로그램종료 하시오. break

# for

r_num = random.randint(1,100)
cnt = 0

for n in range(10):
  num = int(input("숫자입력"))
  if num > r_num:
    print("입력숫자가 더 큼")
  elif num < r_num:
    print("입력숫자가 더 작음")
  else:
    print("정답")
    cnt = 1
    break

if cnt == 0:
  print("탈락")