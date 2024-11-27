from django.shortcuts import render
from board.models import Board
from member.models import Member

## 게시글 삭제
def bdelete(request,bno):
  Board.objects.get(bno=bno).delete()
  context = {"dmsg":bno}
  return render(request,'blist.html',context)
  

## 글 상세보기
def bview(request,bno):
  # npage = request.GET.get("npage",1)
  qs = Board.objects.get(bno=bno)
  context = {"board":qs}
  return render(request,'bview.html',context)


## 글쓰기페이지 / 글쓰기 저장
def bwrite(request):
  if request.method == "GET":
    return render(request,'bwrite.html')
  else:
    id = request.session.get('session_id')
    member = Member.objects.get(id=id)
    btitle = request.POST.get("btitle")
    bcontent = request.POST.get("bcontent") 
    bfile = request.FILES.get("bfile","")

    # 글쓰기 저장
    qs = Board.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile)
    qs.bgroup = qs.bno
    qs.save()

    context = {"wmsg":"1"}
    return render(request,'bwrite.html',context)


## 게시판 리스트
def blist(request):
  qs = Board.objects.all().order_by('-bgroup','bstep')
  context = {"blist":qs}
  return render(request,'blist.html',context)