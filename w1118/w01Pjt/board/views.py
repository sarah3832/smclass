from django.shortcuts import render

# 게시판 호출
def list(request):
  return render(request,'list.html')