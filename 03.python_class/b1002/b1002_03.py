# if - else
# if elif else


# 100~98 A+
# 97~94 A
# 93~90 A-

# 89~88 B+
# 87~84 B
# 83~80 B-

# 79~78 C+
# 77~74 C
# 73~70 C-

# 60점대 D

# 60점미만 F
num = (int(input("점수를 입력하세요.")))

scroe = ""

# if 90<= num:
#   scroe = "A"
#   if 98<= num:
#   scroe += "+"
#   elif 90<== num <=93:
#   scroe += "-"
# elif 80<= num:
#   pass



if 98<= num <= 100:
  print("A+ 입니다.")
elif 94<= num:
  print("A 입니다.")
elif 90<= num:
  print("A- 입니다.")
elif 89== num or num == 88:
  print("B+ 입니다.")
elif 84<= num <= 87:
  print("B 입니다.")
elif 80<= num:
  print("B- 입니다.")
elif 78== num or num == 79:
  print("C+ 입니다.")
elif 74<= num <= 77:
  print("C 입니다.")
elif 70<= num:
  print("C- 입니다.")
elif 60<= num:
  print("D 입니다.")
elif num < 60:
  print("F 입니다.")
else:
  print("점수를 다시 입력하세요.")







# # 3,4,5 - 봄 / 6,7,8 - 여름 / 9,10,11 - 가을 / 12,1,2 - 겨울입니다.
# # 그 외 숫자 - 잘못된 월입니다.
# num = int(input("숫자입력"))
# if 3 <= num <= 5:
#   print("봄 입니다.")
# elif 6 <= num <= 8:
#   print("여름 입니다.")
# elif  9 <= num <= 11:
#   print("가을 입니다.")
# elif  1 <= num <= 2 or num==12:
#   print("겨울 입니다.")
# else:
#   print("잘못된 월이 입력되었습니다.")




# # 입력한 숫자가 10(포함)보다 작거나, 100(포함)보다 클때 정답입니다. 아니면 오답입니다.
# num = int(input("숫자입력"))
# if 10 >= num or 100 <= num:
#   print("정답")
# else:
#   print("오답")



# # 입력한 숫자가 1(포함)보다 크고 10(포함)보다 작을때만 정답입니다. 아니면 오답입니다.
# num = int(input("숫자를 입력"))
# if 1<= num <=10:
#   print("정답입니다.")
# else:
#   print("오답입니다.")



# # 입력한 숫자가 짝수인지, 홀수인지 출력하시오
# num = int(input("숫자를 입력하세요."))
# if num%2 == 0:
#  print("짝수입니다.")
# else:
#  print("홀수입니다.")