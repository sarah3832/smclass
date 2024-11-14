# float타입으로 변경해서 리스트로 저장하시오.
a = ['만','3,450','1.7만','500','1,000']

def chg(val):
  val = val.replace(",","")
  if '만' in val:
    r_val = float(val[:-1])*10000
  else:
    r_val = float(val.replace(",",""))
  return r_val

a_list = list(map(chg,a))
print(a_list)

print(max(a_list))  # 최대값
print(min(a_list))  # 최소값
a_list.sort(reverse=True)  # 역순정렬
print(a_list)

# ---------------

# a = "1.7만"
# if '만' in a:
#   print("있음")
# else:
#   print("없음")