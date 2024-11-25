from django.shortcuts import render,redirect
from member.models import Member

# 로그아웃
def logout(request):
  request.session.clear()
  return redirect('/')


# 로그인페이지 열기, 로그인 확인
def login(request):
  if request.method == 'GET':
    return render(request,'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id,pw=pw)

    if qs:  # 멤버가 있을경우
      request.session['session_id'] = qs[0].id
      request.session['session_nicName'] = qs[0].nicName
      context = {"lmsg":"1"}
    else:  # 멤버가 없을경우
      context = {"lmsg":"0"}

    return render(request,'login.html',context)