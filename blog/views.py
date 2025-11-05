from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from .models import Post

def home(request):
    title = 'Home'
    posts = Post.objects.all()
    data = {
        'posts': posts,
        'title': title
    }
    return render(request, 'blog/home.html',data)

def create(request):
    if(request.method == 'POST'):
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.POST.get('author')
        post = Post(title=title, content=content, author=author)
        post.save()
        return redirect('blog-home')
    else:
        title = 'Create Post'
        data = {
            'title': title
        }
        return render(request, 'blog/create.html', data)

def show(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {
        'title': 'Post Detail',
        'post' : post
    }
    return render(request, 'blog/show.html', data)

def edit(request, post_id):
    if(request.method == 'POST'):
        post = Post.objects.first(id=post_id)
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.objects.update()
        return redirect('blog-post-detail', post_id=post_id)
    else:
        post = Post.objects.first(id=post_id)
        title = 'Edit Post - '+post['title']
        data = {
            'title': title,
            'post' : post
        }
    return render(request, 'blog/edit.html', data)