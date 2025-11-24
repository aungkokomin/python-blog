from django.shortcuts import render, redirect
from django.http import HttpResponse
from ..models import Post, Author
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    title = 'Home'
    posts = Post.objects.all()
    for post in posts:
        post.author_name = Author.objects.get(id=post.author_id).name
    data = {
        'posts': posts,
        'title': title
    }
    return render(request, 'blog/home.html',data)

def create(request):
    authors = Author.objects.all()
    title = 'Create Post'
    data = {
        'title': title,
        'authors': authors
    }
    return render(request, 'blog/create.html', data)

def store(request):
    if request.method == 'POST':
        if request.POST.get('author_id') is None:
            author_id = 1
        else:
            author_id = request.POST.get('author_id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post(title=title, content=content, author_id=author_id)
        post.save()
        return redirect('blog-home')
    else:
        return HttpResponse('Invalid Method')

def show(request, post_id):
    post = Post.objects.get(id=post_id)
    data = {
        'title': 'Post Detail',
        'post' : post
    }
    return render(request, 'blog/show.html', data)

def edit(request, post_id):
    if request.method == 'POST':
        post_data = Post.objects.filter(id=post_id).first()
        post_data.title = request.POST.get('title')
        post_data.content = request.POST.get('content')
        post_data.author_id = request.POST.get('author_id')
        post_data.save()
        return redirect('blog-post-detail', post_id=post_id)
    else:
        post = Post.objects.filter(id=post_id).first()
        authors = Author.objects.all()
        title = 'Edit Post - '+post.title
        data = {
            'title': title,
            'authors': authors,
            'post' : post
        }
    return render(request, 'blog/edit.html', data)

def delete(post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('blog-home')