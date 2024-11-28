from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt  # 예외처리
from member.models import Member
from django.core import serializers # json타입

## 중복확인
def idChk(request):
  id = request.GET.get("id","")
  qs = Member.objects.filter(id=id)
  qs_list = list(qs.values())
  if qs:
    context = {"result":"fail","memeber":qs_list}
  else:
    context = {"result":"success"} 

  return JsonResponse(context)


## 회원가입 03
def step03(request):
  return render(request,'step03.html')


## 로그인 체크
# json타입 변경하려면 - list,dic 타입 / qs:set -> list 타입변경
# @csrf_exempt : 예외처리
def loginChk(request):
  id = request.POST.get("id","")
  pw = request.POST.get("pw","")
  qs = Member.objects.filter(id=id,pw=pw)  # 없으면 None
  if qs:
    print("성공")
    request.session['session_id'] = id
    request.session['session_nicName'] = qs[0].nicName
    qs_list = list(qs.values())
    context = {"result":"success","member":qs_list}
  else:
    print("실패")
    context = {"result":"fail"}

    # qs = Member.objects.get(id=id,pw=pw)  # 없으면 에러
    # json_qs = serializers.serialize('json',[qs])  # json 타입변경

  return JsonResponse(context)


## 로그아웃 페이지
def logout(request):
  request.session.clear()  # 모두삭제 / 1개삭제 : def request.session['session_id']
  context = {"outmsg":"1"}
  return render(request,'index.html',context)


## 로그인 페이지
def login(request):
  return render(request,'login.html')