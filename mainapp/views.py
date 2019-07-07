from django.shortcuts import render, redirect
from .models import Post, Profile #Blog모델을 가져와서 쓸꺼니깐 위에 적어줌
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
    #if user
    posts = Post.objects.all()
    context={
        "posts":posts
        }
    return render(request, 'main.html',context)
        


def write(request): #GET 은 검색을 위함, POST는 데이터를 전송하고 전송된 데이터에 대한 결과값을 돌려받기 위함
    if request.method == "GET":
        return render(request, 'write.html')
    
    elif request.method == "POST":
        post=Post()
        post.user = request.user
        post.title=request.POST['title']
        post.content=request.POST['content']
        post.category=request.POST['category']
        post.npclass=request.POST['npclass']
        try:
            post.image = request.FILES['image']
        except:
            pass
            
        post.save()

        return redirect('main')