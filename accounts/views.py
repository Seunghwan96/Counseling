from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
#
# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(request.POST['id'], password=request.POST['password1'])
            user.profile.name=request.POST['name']
            user.profile.nickname= request.POST['nickname']
            user.profile.sex=request.POST['sex']
            user.profile.birth=request.POST['birth']
            user.profile.phone=request.POST['phone']
            try:
                user.profile.image=request.FILES['image']
            except:
                pass
            auth.login(request, user)
            return redirect('main')
    return render(request, 'signup.html')
 


def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('main') 
    return render(request, 'signup.html')