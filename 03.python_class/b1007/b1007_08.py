import random
lotto = [0]*20+[1]*5
random.shuffle(lotto)

a_list = [
  [1,0,0,0,0],
  [0,1,0,0,0],
  [0,0,1,0,0],
  [0,0,0,1,0],
  [0,0,0,0,1]
]

for i in range(5):
  for j in range(5):
    a_list[i][j] = lotto[5*i+j]

aa_list = [
  ["로또","로또","로또","로또","로또"],
  ["로또","로또","로또","로또","로또"],
  ["로또","로또","로또","로또","로또"],
  ["로또","로또","로또","로또","로또"],
  ["로또","로또","로또","로또","로또"]
]

while True:
  money = int(input("얼마를 배팅 하시겠습니까?>> "))
 
  print("                   [로또 좌표]")
  print("\t0\t1\t2\t3\t4")
  print("-" *50)
  for i in range(5):
    print(i,"|",end="\t")
    for j in range(5):
      print(aa_list[i][j],end="\t")
    print()

  code = input("좌표를 입력하세요.(0.0)>> ")
  codeArr = code.split(".")

  if a_list[int(codeArr[0])][int(codeArr[1])] == 1:
    aa_list[int(codeArr[0])][int(codeArr[1])] = "당첨"
    print(f"{codeArr} 당첨금 : {money*50:,d}")

  else:
    aa_list[int(codeArr[0])][int(codeArr[1])] = "꽝"
    print(f"{codeArr} 다음기회에 : {money}")