from django.shortcuts import render
from member.models import Member

## 회원옵션 페이지
def m2(requset):
  if requset.method == "GET":
    cookmId = requset.COOKIES.get('cookmId','')
    cookMoney = requset.COOKIES.get('cookMoney','')
    cookOption = requset.COOKIES.get('cookOption','')
    context = {"cookmId":cookmId,"cookMoney":cookMoney,"cookOption":cookOption}
    return render(requset,'m2.html',context)
  
  else:
    response = render(requset,'index.html')
    memberId = requset.POST.get('memberId')
    money = requset.POST.get('money')
    option = requset.POST.get('option')
    saveMember = requset.POST.get('saveMember')

    if saveMember is not None:
      response.set_cookie('cookmId',memberId,max_age=60*60)
      response.set_cookie('cookMoney',money,max_age=60*60)
      response.set_cookie('cookOption',option,max_age=60*60)
    else:
      response.delete_cookie('cookmId')
      response.delete_cookie('cookMoney')
      response.delete_cookie('cookOption')

    return response


## 상품구매 페이지
def product(request):
  if request.method == "GET":
    # 쿠키 읽어오기
    cookpId = request.COOKIES.get('cookpId','')
    cookpName = request.COOKIES.get('cookpName','')
    # cookpName = request.COOKIES.get('cookpName','')
    context = {"cookpId":cookpId,"cookpName":cookpName}
    return render(request,'product.html',context)
  
  else:
    # 쿠키저장
    response = render(request,'index.html')
    pId = request.POST.get('pId')
    pName = request.POST.get('pName')
    saveProduct = request.POST.get('saveProduct')

    if saveProduct is not None:
      response.set_cookie('cookpId',pId,max_age=60*60)
      response.set_cookie('cookpName',pName,max_age=60*60)
    else:
      response.delete_cookie('cookpId')
      response.delete_cookie('cookpName')

    return response
    

## 로그인 페이지2
def login2(request):
  if request.method == "GET":
    cookId = request.COOKIES.get('cookId','')
    context = {"cookId":cookId}
    return render(request,'login2.html',context)
  
  else:
    response = render(request,'index.html')
    # 3개 정보
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    saveId = request.POST.get('saveId')

    if saveId is not None:
      response.set_cookie('cookId',id,max_age=60*60)
    else:
      response.delete_cookie('cookId')

    return response


## 로그인 페이지
# 쿠키정보 검색 : request.COOKIES.get('이름')
# 쿠키저장 : response.set_cookie('key','value')
# 쿠키삭제 : response.delete_cookie('key')
def login(request):
  if request.method == "GET":
    print("쿠키정보 : ",request.COOKIES)
    print("cookinfo 쿠키정보 : ",request.COOKIES.get('cookinfo'))
    saveId = request.COOKIES.get('saveId','')
    print("saveId : ",saveId)
    context = {"saveId":saveId}
    response = render(request,'login.html',context)
    
      # 쿠키 설정(저장)
      # max_age : 60초*60분 (브라우저 닫아도 1시간동안 저장) / max_age가 없으면 브라우저 종료시 삭제
      # 1달 = 60*60*24*30 (60초*60분*24시간*30일)
    # 쿠키정보 검색
    if not request.COOKIES.get('cookinfo'):
      response.set_cookie('cookinfo','1111',max_age=60*60)  
    return response
  else:
    print("쿠키정보 : ",request.COOKIES)
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    # pw = request.POST["pw"]  # 값 없을경우, 에러발생
    saveId = request.POST.get("saveId")
    print("전달받은 정보 : ",id,pw,saveId)
    response = render(request,'login.html') 

    # 아이디기억하기 정보가 있으면   
    if saveId is not None :
       response.set_cookie('saveId',id,max_age=60*60) # 아이디기억하기 체크가 있으면, 쿠키저장
    else:
      response.delete_cookie('saveId')  # 아이디기억하기 체크가 없으면, 쿠키삭제

    return response


## 회원전체리스트 페이지
def mlist(request):
  qs = Member.objects.all()
  context = {"mlist":qs}
  return render(request,'mlist.html',context)