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

s_title = ['번호','이름','국어','영어','수학','합계','평균','등수','등록일']




  
    




while True:
  choice = stu_func.main_print()  ## 메인화면출력 부분

  if choice == "1":
    stu_func.stu_insert()  ## 학생성적입력 부분

  elif choice == "2":
    stu_func.stu_output()  ## 학생성적출력 부분

  elif choice == "3":
    stu_func.stu_search()  ## 학생성적검색 부분

  elif choice == "4":
    stu_func.stu_align()

  elif choice == "5":
    print("[ 등수처리 ]")
    sql = "update students a set rank =(select ranks from(select no,rank()over(order by avg desc)ranks from students)b where a.no = b.no)"

      ##### 출력부분 #####
    # db연결
    conn = connects()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    print("등수처리가 완료되었습니다.")
    print()
    #---------------------------------------------
    sql = "select no,name,kor,eng,math,total,round(avg,2),rank,to_char(sdate,'yyyy-mm-dd') from students"
    cursor.execute(sql)
    rows = cursor.fetchall()
    print(f"[ 개수 : {len(rows)} ]")
    for idx,s in enumerate(s_title):
      if idx == 1:
        print(f"{s:12}",end="\t")
        continue
      print(s,end="\t")
    print()
    print("-"*80)
    if len(rows)<1:
      print("데이터가 없습니다.")
      break
    for row in rows:
      for idx,r in enumerate(row):
        if idx == 1:
          print(f"{r:12}",end="\t")
          continue
        print(r,end="\t")
      print()
    print()
    print("데이터 출력완료!")




  elif choice == "0":
    print("프로그램을 종료합니다.")
    break