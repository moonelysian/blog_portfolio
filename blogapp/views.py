from django.shortcuts import render , get_object_or_404 , redirect
from django.utils import timezone
from .models import Blogapp
# Create your views here.
def home(request):
    blogs = Blogapp.objects
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blogapp, pk = blog_id )
    return render(request, 'detail.html',{'blogapp': blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blogapp()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/blogapp/'+str(blog.id))

