from django.urls import path,include  # include 추가
from . import views

app_name = 'board'  # name으로 url연결 시 사용
urlpatterns = [
    path('list/', views.list, name='list'),  # 게시판
]
