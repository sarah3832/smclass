from django.shortcuts import render,redirect
from students.models import Student

def write(request):
  if request.method == 'GET':
    return render(request,'write.html')
  else:
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print("입력데이터 : ",name,major,grade,age,gender)

    Student.objects.crate(name=name,major=major,grade=grade,age=age,gender=gender)
    print("1명 학생저장")
    return redirect("/")