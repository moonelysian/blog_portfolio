from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blogapp
from .forms import BlogPost

def home(request):
    blogs = Blogapp.objects
    #블로그 모든 글 대상으로
    blog_list = Blogapp.objects.all()
    #블로그 객체를 3개씩 자르기
    paginator = Paginator(blog_list, 3)
    #request페이지를 변수에 담아내고
    page = request.GET.get('page')
    #request된 페이지를 가져온 뒤 return
    posts = paginator.get_page(page)
    return render(request, 'home.html', {'blogs': blogs , 'posts' :posts })

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blogapp, pk = blog_id )
    return render(request, 'detail.html',{'blogapp': blog_detail})

def new(request):
    return render(request, 'new.html')

# def create(request):
#     blog = Blogapp()
#     blog.title = request.GET['title']
#     blog.body = request.GET['body']
#     blog.pub_date = timezone.datetime.now()
#     blog.save()
#     return redirect('/blogapp/'+str(blog.id))

def blogpost(request):
    if (request.method == 'POST'):
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date= timezone.now()
            post.save()
            return redirect('/blogapp/'+str(post.id))
    else:
        form = BlogPost()
        return render(request, 'new.html', {'form':form})

def edit(request, blog_id):
    blog = Blogapp.objects.get(pk = blog_id)
    
    if (request.method == 'POST'):
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('/blogapp/'+str(blog.id))
    
    return render(request,'edit.html', {'blog':blog} )

def destroy(request, blog_id ):
    blog = Blogapp.objects.get(pk = blog_id)
    blog.delete()
    return redirect('/')



