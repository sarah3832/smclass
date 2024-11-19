from django.urls import path,include  # include 추가
from . import views

app_name = 'students'  # app_name 설정
urlpatterns = [
    # 방법 3가지 : url링크, views함수호출, name링크
    path('write/', views.write, name='write'), 
    path('search/', views.search, name='search'),  # 검색
    path('list/', views.list, name='list'), 
    path('<str:name>/view/', views.view, name='view'),  # <str:name>을 받아주기 (위치는 view앞,뒤 상관없음)
    path('update/', views.update, name='update'),  # 파라미터 방법
    # path('<str:name>/update/', views.update, name='update'),  
    path('delete/<str:name>/', views.delete, name='delete'),  
]