# 학생성적 프로그램
# 1. 학생성적입력
# 2. 학생성적출력
# 3. 학생성적검색
# studnets테이블 사용
# 시퀀스 students_seq 생성
# 번호,김유신,99,98,96 합계,평균,등수,입력일
# --------------------------------------------
import oracledb
import stu_func


while True:
  choice = stu_func.main_print()  ## 메인화면출력 부분

  if choice == "1":
    stu_func.stu_insert()  ## 학생성적입력 부분

  elif choice == "2":
    stu_func.stu_output()  ## 학생성적출력 부분

  elif choice == "3":
    stu_func.stu_search()  ## 학생성적검색 부분

  elif choice == "4":
    stu_func.stu_align()  ## 학생성적정렬 부분

  elif choice == "5":
    stu_func.stu_rank()  ## 학생등수처리 부분

  elif choice == "0":
    print("프로그램을 종료합니다.")
    break