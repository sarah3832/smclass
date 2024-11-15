from django.urls import path,include  # include 추가
from . import views  # . : 현재폴더

app_name = 'students'  # 앱이름 추가 : 이름으로 접근할때 사용
urlpatterns = [
  # views.py 연결 - 함수호출
  path('write/',views.write,name='write'),  # name : app함수호출 이름
  path('save/',views.save,name='save'), 
  path('list/',views.list,name='list'), 
]
