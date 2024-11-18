from django.urls import path,include  # include 추가
from . import views

app_name = ''  # name으로 url연결 시 사용
urlpatterns = [
    path('', views.index, name='index'),  # 메인페이지 : index, main, default (주로사용)
]
