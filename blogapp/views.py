from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home (request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    print("!!! id : ",blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 DB에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()

    if(blog.title == "" and blog.body == ""):
        error = "ERROR : 제목과 본문을 입력해주세요!"
        return render(request, 'new.html', {'error':error})

    elif(blog.title == ""):
        error = "ERROR : 제목을 입력해주세요!"
        return render(request, 'new.html', {'error':error})

    elif(blog.body == ""):
        error = "ERROR : 본문을 입력해주세요!"
        return render(request, 'new.html', {'error':error})

    blog.save() #DB에 저장 / 삭제 : 객체.delete() 
    return redirect('/blog/'+str(blog.id))

def delete(request, blog_id): #글을 삭제해주는 함수
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.delete()
    return redirect("home")

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()

    return redirect("home.html")

def update_page(request, blog_id): #글을 수정해주는 함수
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "update_page.html", {"blog": blog})