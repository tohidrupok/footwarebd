from django.shortcuts import render
from store.models import NewsArticle
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects.all().order_by('-id')[:6]
    latest_news = NewsArticle.objects.filter(is_availble=True).order_by('-publication_date')[:5]  
    context={
        'latest_news': latest_news ,
        'blogs': blogs
    }
    return render(request, 'home.html',context)

def contact(request):

    return render(request, 'contact.html')

def about(request):

    return render(request, 'about.html')

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs}) 

def blog_detail(request, blog_slug):
    blog = Blog.objects.get(slug=blog_slug)
    return render(request, 'blog_details.html', {'blog': blog}) 