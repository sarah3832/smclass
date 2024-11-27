from django.shortcuts import render
from member.models import Member

## 로그아웃
def logout(request):
  request.session.clear()
  context = {"lmsg":"1"}
  return render(request,'index.html',context)


## 로그인
def login(request):
  if request.method == "GET":
    return render(request,'login.html')
  else:
    id = request.POST.get("id")
    pw = request.POST.get("pw")
    qs = Member.objects.filter(id=id,pw=pw)

    if qs:
      request.session['session_id'] = id
      request.session['session_nicname'] = qs[0].nicname

      context = {"lmsg":"1"}
      return render(request,'login.html',context)
    else:
      context = {"lmsg":"0"}
      return render(request,'login.html',context)
