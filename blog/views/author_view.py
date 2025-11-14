from django.shortcuts import redirect, render
from django.db import models
from ..models import Author

def home(request):
    title = 'Authors'
    authors = Author.objects.all()
    data = {
        'authors': authors,
        'title': title
    }
    return render(request, 'blog/author_home.html', data)

def create(request):
    title = 'Create Author'
    data = {
        'title': title
    }
    return render(request, 'blog/author_create.html', data)

def store(request):
    name = request.POST.get('name')
    address = request.POST.get('address')
    dob = request.POST.get('dob')
    author = Author(name=name, address=address, dob=dob)
    author.save()
    return redirect('blog-author-home')

def edit(request, author_id):
    if(request.method == 'POST'):
        author_data = Author.objects.filter(id=author_id).first()
        author_data.name = request.POST.get('name')
        author_data.address = request.POST.get('address')
        author_data.dob = request.POST.get('dob')
        author_data.save()
        return redirect('blog-author-home')
    else:
        author = Author.objects.filter(id=author_id).first()
        title = 'Edit Author - ' + author.name
        data = {
            'title': title,
            'author': author
        }
        return render(request, 'blog/author_edit.html', data)

def show(request, author_id):
    author = Author.objects.select_related('user').filter(id=author_id).first()
    data = {
        'title': 'Author Detail',
        'author' : author
    }
    return render(request, 'blog/author_show.html', data)

def delete(request, author_id):
    author = Author.objects.get(id=author_id)
    author.delete()
    return redirect('blog-author-home')
