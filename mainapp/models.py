from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #유저
    title = models.CharField(max_length=100) # 제목
    content=models.TextField(blank=True) # 내용
    category = models.CharField(max_length=50, blank=True) #카테고리
    image = models.ImageField(upload_to='images/',null=True, blank=True) #게시글사진첨부
    like_num = models.IntegerField(default=0) #  공감 수
    dislike_num = models.IntegerField(default=0) #   비공감 수
    like_result = models.IntegerField(default=0) #   공감-비공감 = 총점
    report_num = models.IntegerField(default=0) #    신고 횟수
    blind = models.BooleanField(default = False) # 게시글 블라인드 여부
    anonymous = models.BooleanField(default = False) #익명이냐 아니냐
    Report_list = models.TextField(blank=True) # 신고횟수
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now=True)
    Post_list = models.TextField(blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.content[:20]


class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) 
    post = models.ForeignKey(Post,on_delete=models.CASCADE) #Post에서 가져올꺼임. => Post와 COmment가 oneToMany관계를 가짐. 
    content = models.TextField(blank = True)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now = True)
    anonymous = models.BooleanField(default = False) #익명이냐 아니냐
    like_num = models.IntegerField(default=0) #  공감 수
    dislike_num = models.IntegerField(default=0) #   비공감 수
    report_num = models.IntegerField(default=0) #    신고 횟수
    blind = models.BooleanField(default = False) # 게시글 블라인드 여부
    Comment_list= models.TextField(blank=True)

    def __str__(self):
        return self.content

    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=False) #제목
    content = models.TextField(blank=False) #내용
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)


    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) #유저랑 1:1관계
    name=models.CharField(max_length=10) #이름
    nickname=models.CharField(max_length=10) #닉네임
    sex = models.CharField(max_length=5) #성별
    birth = models.CharField(max_length=10) #생년월일
    phone = models.CharField(max_length=15) # 번호
    image = models.ImageField(upload_to='images/',null=True, blank=True) #프로필 사진첨부
    comment_num= models.IntegerField(default=0) #사용자가 작성한 댓글의 수
    subscribe_person = models.IntegerField(default=0) #나를 구돗한 사람들
    like_num = models.IntegerField(default=0) #  공감 받은 횟수
    dislike_num = models.IntegerField(default=0) #   비공감 받은 횟수

    def __str__(self):
        n_user=str(self.user)
        return n_user



@receiver(post_save, sender=User) #자동으로 생성
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()