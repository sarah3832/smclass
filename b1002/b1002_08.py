# 리스트
# in - 데이터가 있는지 확인
# count - 데이터 개수
# find - 데이터가 있는 위치, 없으면 -1 / find(검색어, 시작위치, 끝위치)
# index - 데이터가 있는 위치, 없으면 에러

fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
# 배가 있는 위치를 모두 출력하시오.
search = input("과일 이름을 입력하세요.")
print("모든 글자 : ",fruit)
idx = 0
if fruit.count(search)>0:
 print(f"{search} 글자가 있습니다.")
 for i in range(fruit.count(search)):
   print(f"{search} 글자가 있는 위치 :",fruit.find(search,idx))
   idx = fruit.find(search,idx)+1
else:
 print(f"{search}(이)라는 글자는 없습니다.")




# # count - 문자열 내에 해당개수 확인
# fruit = "사과,배,딸기,포도,복숭아,배,사과,배,딸기"
# # print(fruit.count('사과'))
# # 과일이름을 입력받아 있으면 있습니다, 과일검색개수 : 
# # 없으면 없습니다.
# name = input("과일이름을 입력하세요.")
# if name in fruit:
#   print(f"{name}가(이) 있습니다.")
#   print(f"과일검색개수 : {fruit.count(name)}개") 
#   print(fruit.find(name))
#   # print(fruit.index(name))  # 과일이 있는 위치의 index
# else:
#   print(f"{name}라는 과일이 없어요.")  
#   print(fruit.find(name))     # index 보단 find 
#   # print(fruit.index(name))  # 에러




# count - 리스트에서 개수 확인
# fruit = ['사과','배','딸기','포도','복숭아','배','사과','배','딸기']
# print(fruit.count('배'))
# print(fruit.count('사과'))




# fruit = ['사과','배','딸기','포도','복숭아']
# # 글을 입력받아 입력한 과일이 있으면 있어요, 없으면 없어요.
# name = input("과일을 입력하세요.")
# if name in fruit:
#   print(f"{name}가 있습니다.")
# else:
#   print("없습니다.")  



# fruit = "사과,배,딸기,포도"
# if '배' in fruit:
#   print("배라는 글자가 있어요.") 
# else:
#   print("배라는 글자가 없어요.")



# fruit = ['사과','배','딸기','포도','배']
# if '배' in fruit:  # 한번의 비교로 있는지 확인
#   print("배가 있어요.")
# else:
#   print("배가 없어요.")