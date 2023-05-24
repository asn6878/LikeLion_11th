from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
# Create your views here.
from .models import * 
from .forms import PostCreateForm
import datetime

from django.http import HttpResponse, HttpResponseRedirect

# 과제의 List 구현
def index(request):
    object_list = Post.objects.all().order_by('-id')
    return render(request, 'index.html', {'object_list': object_list})
    
# Create 구현
@csrf_exempt
def post_create(request):
    # if request.method == 'GET':
    #     return render(request, "create.html")
    # elif request.method == 'POST':
    #     title_req = request.POST['title']
    #     content_req = request.POST['content']
    #     # 일단, user와 category는 기본값인 첫번째를 자동으로 사용하게 해두었음.
    #     author_get = User.objects.get(id=1)
    #     category_get = Category.objects.get(id=1)
    #     p = Post(title= title_req, author= author_get, body= content_req, category= category_get)
    #     p.save()
    #     return render(request, "create.html")

    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('post:detail', args=(post.id,)))
    else:
        form = PostCreateForm()
    return render(request, 'create.html',{'form':form})

# Post Detail의 역할. 즉, 한개만 조회하기.
def post_receive(request, pk):
    post = Post.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'detail.html', context)

# Post Update의 역할.
def post_update(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.body = request.POST["body"]
        post.date = datetime.datetime.now()
        post.save()
        return HttpResponseRedirect(reverse('post:detail', args=(post.id,)))
    else:
        context = {'post': post}
        print(post.body)
        print(post.date)
        return render(request, 'update.html', context)
    
# Post Delete의 역할
def post_delete(request, pk):
    Post.objects.filter(id=pk).delete()
    return HttpResponseRedirect(reverse('post:index'))