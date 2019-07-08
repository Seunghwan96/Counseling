from django.shortcuts import render, redirect
from .models import Post, Profile, Comment #Blog모델을 가져와서 쓸꺼니깐 위에 적어줌
from django.core.paginator import Paginator
# Create your views here.
 
# def signup(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                 request.POST['id'], password=request.POST['password1'])
#             user.profile.nickname=request.POST['nickname']
#             user.profile.region = request.POST['region']
            
#             auth.login(request, user)
#             return redirect('main')
#     return render(request, 'signup.html')
    # paginator = Paginator(posts,5)
    # now_page = request.GET.get('page')
    # posts = paginator.get_page(now_page)
    
def main(request):
    posts = Post.objects.all()
    context={
        "posts":posts
        }
    return render(request, 'main.html',context)

def profile(request, user):
    profile = Profile.objects.get(user = request.user)
    context={
        "profile":profile
        }   
    return render(request, 'profile.html', context)

def write(request): #GET 은 검색을 위함, POST는 데이터를 전송하고 전송된 데이터에 대한 결과값을 돌려받기 위함
    if request.method == "GET":
        return render(request, 'write.html')
    
    elif request.method == "POST":
        post=Post()
        post.user = request.user
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.category=request.POST['category']
        try:
            post.image = request.FILES['image']
        except:
            pass
            
        post.save()

        return redirect('main')

def read(request,post_id):
    post = Post.objects.get(id=post_id)
    comment = Comment.objects.filter(post = post_id)
    context = {
        "post":post,
        "comment":comment,
    }
    return render(request,'read.html',context)

def delete(request,post_id):
    post = Post.objects.get(id = post_id)
    post.delete()
    return redirect(main)


def c_create(request,post_id):
    if request.method == "POST":
        comment = Comment()
        comment.user = request.user
        comment.post = Post.objects.get(id = post_id)
        comment.content = request.POST['comment']
        anonymous = request.POST.get('anonymous', False)
        if anonymous == "y":
            comment.anonymous = True
        comment.save()
        return redirect(read,comment.post.id)

def c_delete(request,comment_id):
    comment = Comment.objects.get(id = comment_id)
    post_id = comment.post_id
    comment.delete()
    return redirect(read,post_id)