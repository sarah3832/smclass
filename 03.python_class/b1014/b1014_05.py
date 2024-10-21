subName = ["국어","영어","수학"]
score = {"국어":100,"영어":95,"수학":80}
print(score)
print(score['국어'])
print(subName[0])
print(score[subName[0]])

# 둘다 가능
for k,v in score.items():
  print(k,":",v)

# for i in subName:
#   print(i,":",score[i])









# def gugudan(n):
#   for i in range(2,n+1):
#     print("[ {} 단 ]".format(i))
#     for j in range(2,10):
#       print("{} * {} = {}".format(i,j,i*j))


# nArr = [9,5,7]
# # 2-9 , 2-5, 2-7
# # gugudan(9)
# # gugudan(5)
# # gugudan(7)

# for i in nArr:
#   gugudan(i)
#   print("-"*50)





# # 구구단을 출력하시오.
# def gugudan(n1,n2):
#   for i in range(n1,n2+1):
#     print("[ {} 단 ]".format(i))
#     for j in range(2,10):
#       print("{} * {} = {}".format(i,j,i*j))

# # 2-5단
# gugudan(2,5)

# # 3-9단
# gugudan(3,9)

# # 5-8단
# gugudan(5,8)