from django.shortcuts import render,redirect
from board.models import Board  # 추가
from django.db.models import Max  # 추가
from django.contrib import messages  # 추가
from django.db.models import F  # 추가(f함수)

## 답변달기
def breply(request,bno):
  if request.method == "GET":
    print("게시글 번호 : ",bno)
    qs = Board.objects.get(bno=bno)
    context = {"board":qs}
    return render(request,'breply.html',context)
  else:
    bgroup = int(request.POST.get("bgroup"))  # str타입 -> int타입 변경
    bstep = int(request.POST.get("bstep"))
    bindent = int(request.POST.get("bindent"))
    id = request.POST.get("id")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    print("bgroup 번호 : ",bgroup)

    # 다른 답변달기에 bstep을 1씩 증가시켜줌
    qs = Board.objects.filter(bgroup=bgroup,bstep__gt=bstep)
    qs.update(bstep=F('bstep')+1)

    # bgroup : 부모의 bgroup 입력
    Board.objects.create(id=id,btitle=btitle,bcontent=bcontent,bgroup=bgroup,bstep=bstep+1,bindent=bindent+1)

    # return redirect('board:blist')
    return render(request,'blist.html',{"r_msg":"1"})


## 글 삭제
def bdelete(request,bno):
  print("게시글 번호 : ",bno)
  Board.objects.get(bno=bno).delete()
  return render(request,'blist.html',{"d_msg":bno})


## 글수정페이지, 글수정 저장
def bmodify(request,bno):
  print("게시글 번호 : ",bno)
  if request.method == "GET":
    qs = Board.objects.filter(bno=bno)
    context = {"board":qs[0]}
    return render(request,'bmodify.html',context)
  else:  #post
    bno = request.POST.get("bno")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    qs = Board.objects.get(bno=bno)
    qs.btitle = btitle
    qs.bcontent = bcontent
    qs.save()
    # return redirect("board:blist")
    return render(request,'bmodify.html',{'u_msg':bno})


## 글 상세보기
def bview(request,bno):
  print("게시글 번호 : ",bno)

  # 조휘수 1증가 - get : save()
  # qs = Board.objects.get(bno=bno)
  # qs.bhit += 1
  # qs.save()
  # context = {'board':qs}

  # 조휘수 1증가 - filter : update()
  qs = Board.objects.filter(bno=bno)
  qs.update(bhit=F('bhit')+1)
  context = {'board':qs[0]}

  return render(request,'bview.html',context)


## 게시판 글쓰기페이지, 글쓰기저장
def bwrite(request):
  if request.method == "GET":
    return render(request,'bwrite.html')
  else:
    id = request.POST.get("id")
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent")
    # no = Board.objects.aggregate(max_bno = Max('bno'))
    # no['max_bno']+1
    # 오라클 sequence.nextval, sequence.currval

    # bno,bstep,bindent,bhit,bdate - 자동
    # id,btitle,bcontent,bgroup - 입력

    # DB저장
    qs = Board.objects.create(id=id,btitle=btitle,bcontent=bcontent)
    qs.bgroup = qs.bno
    qs.save()
    # 1회만 노출
    messages.success(request,message='게시글이 저장되었습니다.')
    # return redirect('board:blist')
    return render(request,'bwrite.html',{'w_msg':'1'})


## 게시판 리스트
def blist(request):
  qs = Board.objects.all().order_by("-bgroup","bstep")
  context = {"blist":qs}
  return render(request,'blist.html',context)