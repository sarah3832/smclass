from django.urls import path,include  ## include 추가
from .import views  ## 추가 (.은 현재폴더를 의미)

#### 메인 URL ####
app_name = 'students'  ## app_name 추가
urlpatterns = [
    path('write/',views.write,name='write'),
]
