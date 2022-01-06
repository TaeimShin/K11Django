from .models import Post
from django.core import paginator
from django.shortcuts import redirect, render
import os
from django.conf import settings
from django.core.paginator import Paginator

def index(request):
    return render(request,'boardApps/index.html')

def list(request):
    page = request.GET.get('page','1')
    postlist = Post.objects.all().order_by('-id')
    
    paginator = Paginator(postlist,10)
    postlist = paginator.get_page(page)
    return render(request,'boardApps/list.html',{'postlist':postlist})

def write(request):
    if request.method=="POST":
        # 페이징 처리를 위한 더미데이터 200개 입력시 사용
        #for i in range(200):
        try :
        
            Post.objects.create(
                titles = request.POST['titles'],
                #titles = request.POST['titles'] + "-" + str(i),
                contents = request.POST['contents'],
                name1 = request.POST['name1'],
                mainphoto=request.FILES['mainphoto'],
            )
        except:         
            Post.objects.create(
                titles = request.POST['titles'],
                #titles = request.POST['titles'] + "-" + str(i),
                contents = request.POST['contents'],
                name1 = request.POST['name1'],
            )
        return redirect('../list')

    return render(request, 'boardApps/write.html')

def view(request, pk):
    print("adddddsdf")
    post = Post.objects.get(pk=pk)
    print("asdf")
    return render(request, 'boardApps/view.html', {'post':post})


def edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method=="POST":
        try :
                post.titles = request.POST['titles']
                post.contents = request.POST['contents']
                post.name1 = request.POST['name1']
                post.mainphoto=request.FILES['mainphoto']
                
                print(os.path.join(settings.MEDIA_ROOT, request.POST['prevphoto']))
                os.remove(os.path.join(settings.MEDIA_ROOT, request.POST['prevphoto']))
        except:
                post.titles = request.POST['titles']
                post.contents = request.POST['contents']
                post.name1 = request.POST['name1']
        post.save()
        return redirect('/boardApps/view/'+str(pk))
    else :
        return render(request, 'boardApps/edit.html',{'post':post})
    
def delete(request,pk):
    post = Post.objects.get(pk=pk)
    if request.method=="GET":
        # 게시물 삭제
        post.delete()
        return redirect('../list')