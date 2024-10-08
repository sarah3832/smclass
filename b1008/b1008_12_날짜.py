import datetime

today = datetime.datetime.now()
# 날짜,시간,밀리초
print(today)

# 날짜 포맷
now_data = today.strftime("%Y-%m-%d")
print(now_data)
print(type(now_data))  # 포맷을 사용하면 타입은 모두 str

now_datatime = today.strftime("%Y-%m-%d %H:%M:%S")
print(now_datatime)