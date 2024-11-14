# 파일 입출력
# 1)파일열기 2)읽기및쓰기 3)파일닫기
# 변수명 = open(파일명,r)  -  읽기
# 변수명 = open(파일명,w)  -  덮어쓰기
# 변수명 = open(파일명,a)  -  이어쓰기
# 변수명 = open(파일명,b)  -  이진모드,이진파일처리
# 변수명.close()
# 파일읽기 - r
# 위치에 파일이 없으면 에러
# 가장 바깥 폴더의 위치에서 파일을 찾음
# f = open('a.txt','r',encoding='UTF-8')
### 1. readline() - 한줄씩 읽음
# 절대경로를 사용
# f = open('C:/aaa/a.txt','r',encoding='UTF-8')
# 한줄만 읽음
# line = f.readline()
# print(line)
# f.close()
# f = open('C:/aaa/a.txt','r',encoding='UTF-8')
# while True:
#   line = f.readline()
#   if not line:break
#   print(line.strip())  # \n 값을 생략
# f.close()
### 2. readlines() - 모든 글 읽음
# readlines()가 readline() 보다 빠르지만 읽는 양이 많아지면 메모리 부하가 올 수 있다
# f = open('a.txt','r',encoding='UTF-8')
# lines = f.readlines()
# # print(type(lines))  # -> 리스트
# for line in lines:
#   print(line.strip())
# f.close()
### 3. read()
# f = open('a.txt','r',encoding='utf-8')
# # print(type(f))
# for line in f:
#   print(line.strip())
# f.close()
### 파일 쓰기 - w -> 파일 생성 후 글자 입력
# f = open('aa.txt','w',encoding='utf-8')
# f.write("안녕하세요1\n")
# f.write("안녕하세요2\n")
# f.write("안녕하3\n")
# f.close()
# print("글쓰기 종료")
# f = open('aa.txt','w',encoding='utf-8')
# for i in range(1,10+1):
#   data = f"안녕하세요.{i}\n"
#   f.write(data)
# f.close()
# print("글쓰기 종료")
# while True:
#   print("[메모장]")
#   data = input("저장하려는 글자를 입력하세요.>> ")
#   f = open('aa.txt','w',encoding = 'utf-8')
#   f.write(data)
#   f.close
### 파일 이어 쓰기 - a -> 이어쓰기
# while True:
#   print("[메모장]")
#   data = input("저장하려는 글자를 입력하세요.>> ")
#   f = open('aa.txt','a',encoding = 'utf-8')
#   f.write(data+"\n")
#   f.close
### 파일 with
# close()를 하지 않아도 됨
with open ("aa.txt","w",encoding="utf-8") as f:
  f.write("안녕하세요")