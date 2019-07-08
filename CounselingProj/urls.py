"""CounselingProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
import mainapp.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainapp.views.main, name='main'),
    path('write/', mainapp.views.write, name='write'),
    path('read/<int:post_id>',mainapp.views.read,name='read'),
    path('delete/<int:post_id>',mainapp.views.delete,name='delete'),
    path('signup/', accounts.views.signup, name='signup'),
    path('login/', accounts.views.login,name='login'),
    path('logout/', accounts.views.logout, name='logout'),
    path('profile/<str:user>',mainapp.views.profile, name='profile'),
    path('c_create/<int:post_id>',mainapp.views.c_create, name="c_create"),
    path('c_delete/<int:comment_id>',mainapp.views.c_delete, name='c_delete'),
]
