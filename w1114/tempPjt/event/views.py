from django.shortcuts import render

# Create your views here.
def eventView(request):  # request 무조건
  return render(request,'eventView.html') 