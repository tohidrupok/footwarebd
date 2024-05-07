from django.shortcuts import render
from store.models import NewsArticle

# Create your views here.
def home(request):
    latest_news = NewsArticle.objects.filter(is_availble=True).order_by('-publication_date')[:5] 
    return render(request, 'home.html',{'latest_news': latest_news,})

def contact(request):

    return render(request, 'contact.html')

def about(request):

    return render(request, 'about.html')

def blog(request):
    

    return render(request, 'blog.html')