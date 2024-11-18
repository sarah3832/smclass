from django.contrib import admin
from django.urls import path,include  # include 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),  # urls 추가
    path('', include('home.urls')),  # urls 추가
    path('board/', include('board.urls')),  # urls 추가
]
