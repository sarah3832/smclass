from django.shortcuts import render

# Create your views here.
def eventpage(request):
  return render(request,'eventpage.html')
