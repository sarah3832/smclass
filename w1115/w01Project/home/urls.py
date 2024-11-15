from django.urls import path,include  # include 추가
from . import views  # . : 현재폴더

app_name = ''  # 앱이름 추가 : 이름으로 접근할때 사용
urlpatterns = [
  # views.py 연결 - 함수호출
  path('',views.index,name='index')  # name : app함수호출 이름
]
