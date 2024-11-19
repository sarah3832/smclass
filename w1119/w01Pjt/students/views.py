from django.shortcuts import render,redirect  # redirect 추가
from students.models import Student  # models 추가
from django.urls import reverse

## 학생정보 검색
def search(request):
  search = request.GET.get('search')
  print("검색 단어 search : ",search)
  # 데이터검색 부분
  qs = Student.objects.filter(name__contains=search)
  context = {"slist":qs}
  return render(request,'list.html',context)


## 학생정보 삭제
def delete(request,name):                           
  print("삭제정보 이름 : ",name)
  Student.objects.get(name=name).delete()
  return redirect('/students/list')


## 1.학생수정페이지, 2.학생수정 저장
def update(request):
  if request.method == "GET":
    name = request.GET['name']
    print(name)
    qs = Student.objects.get(name=name)
    context = {"stu":qs}
    return render(request,'update.html',context)
  else:
    name = request.POST.get('name')
    major = request.POST.get('major')
    grade = request.POST.get('grade')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    hobby = request.POST.getlist('hobby')

    # Student 검색
    qs = Student.objects.get(name=name)
    qs.major = major
    qs.grade = grade
    qs.age = age
    qs.gender = gender
    qs.hobby = hobby
    qs.save()

    return redirect('students:view',name,)
    # return redirect(reverse('students:view',args=(name,)))


## 학생상세보기
def view(request,name):
  qs = Student.objects.get(name=name)
  context = {"stu":qs}
  return render(request,'view.html',context)


## 학생리스트
def list(request):
  # 학생전체정보 가져오기
  # qs = Student.objects.all()
  qs = Student.objects.order_by('-grade','name')  # 학년 순으로 정렬
  context = {"slist":qs}
  return render(request,'list.html',context)


## 1.학생입력페이지 열기, 2.학생정보 저장
def write(request):
  if request.method == "POST":
    name = request.POST.get('name')  # 데이터가 없을때, None
    major = request.POST['major']  # 데이터가 없을때, 에러
    grade = request.POST['grade']  
    age = request.POST['age']  
    gender = request.POST['gender']  
    # hobby = request.POST['hobby']  # checkbox데이터 1개만 가져옴
    hobbys = request.POST.getlist('hobby')  # getlist : checkbox데이터들 다 가져옴
    # hobby = ','.join(hobbys)  # list -> str타입으로 변경
    # hobby_list = hobby.split(",")  # str -> list타입으로 변경

    print(name)  
    # print("hobby : ",hobby)  
    print("hobbys 복수 : ",hobbys) 

    ## qs.save() 방법
    qs = Student(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)
    qs.save()

    ## create() 방법 : save() 필요없음
    # Student.objects.create(name=name,major=major,grade=grade,age=age,gender=gender,hobby=hobbys)

    return redirect('/students/list')

  else:  # GET호출
    # templates 폴더에서 html파일 검색
    return render(request,'write.html')