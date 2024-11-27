from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from member.models import Member

## 아이디 체크 / ajax 통신
def idChk(request):
  id = request.GET.get("id","")
  print("id : ",id)
  context = {"id":id, "result":"success"}
  return JsonResponse(context)


## 회원가입 2
def join02(request):
  return render(request,'join02.html')

## 회원가입 1
def join01(request):
  return render(request,'join01.html')


## ajax 통신
# @csrf_exempt  # csrf_token 예외처리
def loginChk(request):
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  print("html에서 넘어온 데이터 : ",id, pw)

  # get 검색 
  # qs = list(Member.objects.get(id=id,pw=pw).values())
  # if qs:
  #   context = {"member":qs, "result":"success"}
  # else:
  #   context = {"result":"fail"}
  # return JsonResponse(context)

  # filter 검색 / 객체 보내는 방법 : list타입으로 보내야함 (타입에러 발생)
  qs = list(Member.objects.filter(id=id,pw=pw).values())
  if qs:
    context = {"member":qs, "result":"success"}
  else:
    context = {"result":"fail"}
  return JsonResponse(context)

  # # 변수 보내는 방법
  # qs = Member.objects.filter(id=id,pw=pw)
  # if qs:
  #   context = {"id":qs[0].id, "nicName":qs[0].nicName, "pw":pw, "result":"success"}
  # else:
  #   context = {"result":"fail"}
  # return JsonResponse(context)


## 로그인
def login(request):
  return render(request,'login.html')