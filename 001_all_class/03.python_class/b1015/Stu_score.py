# import  S_func  # 불러오기
from S_func import *  # 모든 함수를 다 가져오기 (*사용)




# -------------------------- 프로그램 시작 -------------------------------------

# 학생성적프로그램
while True:
  choice = title_program()    # 메뉴출력함수 호출

  if choice == "1":
    stuNo = stu_input(stuNo)  # 학생성적입력함수 호출   

  elif choice == "2":
    stu_output(students)  # 학생성적출력함수 호출

  elif choice == "3":
    stu_update(students)  # 학생성적수정함수 호출

  elif choice == "4":
    stu_select(students)  # 학생성적검색함수 호출

  elif choice == "5":
    stu_delete(students)  # 학생성적삭제함수 호출

  elif choice == "6":
    stu_rank(students)  # 학생성적 등수처리함수 호출

  elif choice == "7":
    stu_sort(students)  # 학생성적정렬함수 호출
# --------------------------------------------    


    


    

    









# 학생성적 입력부분을 구현하시오.
# dict 타입으로 입력할 것
# 번호,이름,국어,영어,수학,합계,평균,등수
# 입력이 완료되면 출력이 바로 되도록 하시오.

# print("[ 학생성적입력 ]")
# name = input("이름을 입력하세요.")

