import os

f = open("b1017/cart.txt","r",encoding="utf-8")
while True:
  line = f.readline()
  if not line : break
  print(line.strip())


# isfile : 파일인지 확인 / isdir : 디렉토리인지 확인 / exists : 파일이 존재하는지
# if os.path.isfile("b1017/students.txt"):
#   print("파일이 존재합니다.")
# else:
#   print("파일이 존재하지 않습니다.")