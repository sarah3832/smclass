stu_title = ['번호','이름','국어','영어','수학','과학','합계','평균']
stu_datas = [
[1,'최연준',100,100,100,99],
[2,'최범규',100,99,98,99],
[3,'최수빈',80,100,90,99],
[4,'김용준',80,80,90,100],
[5,'강태현',70,100,80,69],
]

# for문
for s_t in stu_title:
  print("{}".format(s_t),end='\t')
print()
print("-"*60)

for s in stu_datas:
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format
        (s[0],s[1],s[2],s[3],s[4],s[5],
        s[2]+s[3]+s[4]+s[5],
        (s[2]+s[3]+s[4]+s[5])/4))