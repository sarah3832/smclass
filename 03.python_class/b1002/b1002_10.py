fruit = []

while True:     
  # strip() 앞쪽여백, 뒤쪽여백 제거 trim ' 사과' -> '사과'
  # "사 과" -> '사 과
  # replace(" ","") : 문자 대체함수
  search = input("과일이름을 입력하세요.(종료x)").replace(" ","")
  # search = input("과일이름을 입력하세요.(종료x)").strip()
  if(search == 'x'):
    break
  
  # 입력된 과일이름을 리스트에 추가하시오.
  if search in fruit:
    print("같은 이름이 있습니다.")
    # print("모든 과일이름 :",fruit)  
  else:
    print(f"{search}을(를) 추가합니다.")
    fruit.append(search)
    print("모든 과일이름 :",fruit)  



# break : 반복문을 종료할때
# while True:
#   break
# print("프로그램 종료")


# a = 0
# while True:  # while True : 무한반복
#   print(a)
#   a += 1

# while a<10:
#   a += 1
#   print(a)

# print("프로그램 종료")