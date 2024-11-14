from django.urls import path,include
from . import views

app_name = ''
urlpatterns = [
    ### url 주소 / views.py 함수명 / url 이름
    ## 연결 2가지 방식
    # http://127.0.0.1:8000/students/reg/ (외부에서 접속할때)
    # students:reg (프로그램 내에서 사용)
    path('',views.index,name='index'),
]
