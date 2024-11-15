from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect  ## 추가
from django.urls import reverse  ## 추가
from students.models import Student  ## 추가

def list(request):
  qs =Student.objects.all()
  context = {"list":qs}
  return render(request,'stu_list.html',context)


## 1.write페이지 열기,2.write 학생정보 저장
def write(request):
  if request.method == "GET":
    print("write GET방식 호출")
    return render(request,'stu_write.html')
  else:
    print("write POST방식 호출")
    name = request.POST['name']
    major = request.POST['major']
    grade = request.POST['grade']
    age = request.POST['age']
    gender = request.POST['gender']
    print(name,major,grade,age,gender)
    # qs = Student(s_name=name,s_major=major,s_grade=grade,s_age=age,s_gender=gender)
    # qs.save()
    return redirect('index')





# def write(request):
#   return render(request,'stu_write.html')


# def save(request):
#   print("학생정보저장 호출")
#   if request.POST == 'POST':
#     print("post1")
#   else:
#     print("get : ",request.GET)

#   if request.GET:
#     print("get2 : ",request.GET)

#   if request.POST:
#     print("post2")
#     name = request.POST['name']
#     major = request.POST['major']
#     grade = request.POST['grade']
#     age = request.POST['age']
#     gender = request.POST['gender']
#     print(name,major,grade,age,gender)
#     qs = Student(s_name=name,s_major=major,s_grade=grade,s_age=age,s_gender=gender)
#     qs.save()
#   return HttpResponseRedirect(reverse('index'))