from django.shortcuts import redirect, render
from .models import Post

# 게시판 앱의 첫화면
def index(request):
    return render(request,'board/index.html')

# 게시판 목록
def list(request):
    # Post테이블의 모든 레코드를 id(일련번호:pk)의 내림차순으로 가져온다.
    postlist = Post.objects.all().order_by('-id')
    #템플릿을 렌더링 한다.
    return render(request,'board/list.html',{'postlist':postlist})

#글쓰기 
def write(request):
    # 전송방식이 POST라면 submit이므로 폼값을 테이블에 입력한다
    if request.method=="POST":
        try :
            # 파일첨부가 있는 경우 여기서 insert됨
            Post.objects.create(
                titles = request.POST['titles'],
                contents = request.POST['contents'],
                # 파일첨부를 하지 않으면 여기서 예외발생됨
                mainphoto=request.FILES['mainphoto'],
            )
        except:
            # 파일첨부를 하지 않은 경우이므로 제목과 내용만 입력함
            Post.objects.create(
                titles = request.POST['titles'],
                contents = request.POST['contents'],
            )
            # create()를 통해 insert처리
        #입력이 처리되었다면 리스트로 이동한다.
        return redirect('../list')
    # 전송방식이 GET이라면 글쓰기 페이지로 진입한다.
    return render(request, 'board/write.html')

# 글 상세보기
def view(request, pk):
    # 일련번호에 해당하는 게시물 하나를 select한다
    post = Post.objects.get(pk=pk)
    return render(request, 'board/view.html',{'post':post})

# 글 수정하기
def edit(request, pk):
    # 일련번호를 통해 기존 게시물 가져오기
    post = Post.objects.get(pk=pk)
    if request.method=="POST":
        try :
                post.titles = request.POST['titles']
                post.contents = request.POST['contents']
                post.mainphoto=request.FILES['mainphoto']
        except:
                post.titles = request.POST['titles']
                post.contents = request.POST['contents']
        # 폼값 처리후 save()함수를 통해 update처리함
        post.save()
        # 수정처리가 완료되면 상세보기 페이지로 이동함
        return redirect('../view/'+str(pk))
    else :
        # 전송방식이 GET이라면 수정하기로 진입함
        return render(request, 'board/edit.html',{'post':post})

def delete(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method=="GET":
        # 게시물 삭제
        post.delete()
        return redirect('../list')