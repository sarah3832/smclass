from django.contrib import admin
from django.urls import path,include  # include 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),  # 연결
    path('', include('home.urls')),  # 연결
]
