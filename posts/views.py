from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm, RawPostForm
# Create your views here.
def index(request):
  posts = Post.objects.all()
  options = {
    'posts': posts
  }
  return render(request, 'index.html', options)
def show(request, id):
  post = Post.objects.get(id=id)
  options = {
    'post': post
  }
  return render(request, 'show.html', options)
def create(request):
  form = RawPostForm(request.POST or None)
  if form.is_valid():
    post = Post.objects.create(**form.cleaned_data)
    post.save()
    return redirect('/posts')
  options = {
    'form': form
  }
  return render(request, 'new.html', options)
def edit(request, id):
  post = Post.objects.get(id=id)
  form = PostForm(request.POST or None, instance=post)
  if form.is_valid():
    form.save()
    return redirect('/posts')
  options = {
    'form': form
  }
  return render(request, 'edit.html', options)

    
def destroy(request, id):
  if request.method == 'POST':
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/posts')