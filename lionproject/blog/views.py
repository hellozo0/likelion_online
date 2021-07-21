from django.shortcuts import render,redirect, get_object_or_404 
from django.utils import timezone #추가
from .models import Blog 
from .forms import BlogForm

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs' : blogs})

def detail(request, id):  
    blog = get_object_or_404(Blog,pk=id) 
    return render(request, 'detail.html', {'blog' : blog})

def new(request):
    form = BlogForm()
    return render(request, 'new.html', {'form':form})

def create(request):
    form = BlogForm(request.POST,request.FILES)
    if form.is_valid(): #유효성 검사
        new_blog = form.save(commit=False) #pub_date 추가가 안되었기에... 임시 저장
        new_blog.pub_date = timezone.now()
        new_blog.save()
        return redirect('detail', new_blog.id) 
    return redirect('home') #실패 했을 경우 home으로

def edit(request, id):
    edit_blog = Blog.objects.get(id=id)
    return render(request, 'edit.html', {'blog' : edit_blog})

def update(request,id):
    update_blog = Blog.objects.get(id=id)
    update_blog.title = request.POST['title']
    update_blog.writer = request.POST['writer']
    update_blog.body = request.POST['body']
    update_blog.pub_date = timezone.now()
    update_blog.save() 
    return redirect('detail', update_blog.id) 

def delete(request,id):
    delete_blog = Blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')
