from django.shortcuts import render

# Create your views here.
def studentspage(request):
  return render(request,'studentspage.html')
