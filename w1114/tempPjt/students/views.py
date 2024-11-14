from django.shortcuts import render

# Create your views here.
def regStudent(request):  # request 무조건
  return render(request,'register.html')
