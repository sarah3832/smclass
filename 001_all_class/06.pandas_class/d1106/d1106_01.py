# 데이터분석 - pandas : 문자,수치 가능 / numpy : 수치만 가능
# 시각화 : matplotlib
# pandas 설치 : pip install pandas
# matplotlib 설치 : pip install matplotlib
# 엑셀파일 열기 : pip install xlrd -> pip install openpyxl

import pandas as pd

# 1차원 - series / 2차원 - DataFrame

# series
# 차원 (정수,실수,문자열 등)
temp = pd.Series([-20,-10,10,20],index=['Jan','Feb','Mar','Apr'])
print(temp)

print(temp['Jan'])
print(temp['Feb'])
print(temp['Mar'])

# a = [10,20,30,40]
# print(a)