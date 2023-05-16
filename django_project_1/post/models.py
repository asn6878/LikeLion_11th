from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime

class Blog(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_time = models.DateTimeField('date created')
    blog_profile = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Today(models.Model): # 블로그의 방문자 수를 나타내는 클래스
    today_day = models.IntegerField(default=0) # 당일 방문객 수
    today_total = models.IntegerField(default=0) # total 방문객 수
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return "금일 방문자" + str(self.today_total)

class Category(models.Model): # 게시물을 분류할 수 있는 카테고리
    name = models.CharField(max_length=30)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True) # 날짜
    likes = models.IntegerField(default=0) # 좋아요
    dislikes = models.IntegerField(default=0) # 싫어요

    def __str__(self):
        return self.comment

class Tag(models.Model): # 게시글에 달리는 태그(해시태그)
    tag = models.CharField(max_length=30)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag

