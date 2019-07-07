from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE) #유저
    #npclass = models.CharField(max_length=20) # 클래스(노말인지 프리미엄인지) 프리미엄(계급?) 은 그냥 인기많은사람임.  이건 없앨예정 네이
    title = models.CharField(max_length=100) # 제목
    content=models.TextField(blank=True) # 내용
    category = models.CharField(max_length=50, blank=True) #카테고리
    image = models.ImageField(upload_to='images/',null=True, blank=True) #게시글사진첨부
    like_num = models.IntegerField(default=0) #  공감 수
    dislike_num = models.IntegerField(default=0) #   비공감 수
    like_result = models.IntegerField(default=0) #   공감-비공감 = 총점
    report_num = models.IntegerField(default=0) #    신고 횟수
    blind = models.BooleanField(default = False) # 게시글 블라인드 여부
    created_at = models.DateField(auto_now_add = True)
    updated_at = models.DateField(auto_now=True)

    def setLike_num(self): # 공감 버튼 누를 시 호출
        self.like_num += 1
        setLike_result()

    def setDislike_num(self): # 비공감 버튼 누를 시 호출
        self.dislike_num += 1
        setLike_result()

    def setLike_result(self): # 총점 계산기 : 공감 및 비공 누를 시 호출
        self.like_result = (self.like_num - self.dislike_num)

    def setReport_num(self): # 신고 버튼 누를 시 호출
        self.report_num += 1
        checkReport()
        
    def checkReport(self): # 신고 횟수가 5번 넘어가면 블라인드 처리
        if self.report_num == 5: # boolean 변수인 blind를 보고 판단하여 블라인드 처리
            self.blind = True

    def __str__(self):
        return self.title


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
    def setLike_num(self): # 공감 버튼 누를 시 호출
        self.like_num += 1
        setLike_result()

    def setDislike_num(self): # 비공감 버튼 누를 시 호출
        self.dislike_num += 1
        setLike_result()

    def setLike_result(self): # 총점 계산기 : 공감 및 비공 누를 시 호출
        self.like_result = (self.like_num - self.dislike_num)

    def setReport_num(self): # 신고 버튼 누를 시 호출
        self.report_num += 1
        checkReport()
        
    def checkReport(self): # 신고 횟수가 5번 넘어가면 블라인드 처리
        if self.report_num == 5: # boolean 변수인 blind를 보고 판단하여 블라인드 처리
            self.blind = True

    def __str__(self):
        return self.content

class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE) #유저랑 1:1관계
    image = models.ImageField(upload_to='images/',null=True, blank=True) #프로필 사진첨부
    comment_num= models.IntegerField(default=0) #사용자가 작성한 댓글의 수
    subscribe_person = models.IntegerField(default=0) #나를 구돗한 사람들
    like_num = models.IntegerField(default=0) #  공감 받은 횟수
    dislike_num = models.IntegerField(default=0) #   비공감 받은 횟수

    def setProfile_picture(self): #사진프로필 출력
        pass
    def addPost_num(self): #게시글수 증가
        pass
    def subPost_num(self): #게시글수 감소
        pass
    def setComment_num(self): #댓글수 증가
        pass
    def setLike_num(self): #댓글수 감소
        pass
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