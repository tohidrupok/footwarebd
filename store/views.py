from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Company, NewsArticle, Leaders , Factory, InternationaCompany, Event, Gallery 
from django.db.models import Q

def company_list(request):
    all_companies = Company.objects.all()

    paginator = Paginator(all_companies, 40)  # 40 companies per page
    page = request.GET.get('page')

    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        companies = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        companies = paginator.page(paginator.num_pages)

    return render(request, 'store/company_list.html', {'companies': companies})

def company_detail(request, company_slug):
    company = Company.objects.get(slug=company_slug)
    map_url = company.generate_map_url()
    context = {
        'company': company,
        'map_url': map_url
    }
    return render(request, 'store/details.html', context)  

def factorys_list(request): 
    count = Factory.objects.count()
    factorys = Factory.objects.all()  
    paginator = Paginator(factorys, 61)  # 61 companies per page
    page = request.GET.get('page')

    try:
        factorys = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        factorys = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        factorys = paginator.page(paginator.num_pages)

    return render(request, 'store/factorys_list.html', {'factorys': factorys,'count': count})  

def internation_company_list(request): 
    count = InternationaCompany.objects.count()
    company = InternationaCompany.objects.all()  
    paginator = Paginator(company, 61) 
    page = request.GET.get('page')

    try:
        company = paginator.page(page)
    except PageNotAnInteger:
        
        company = paginator.page(1)
    except EmptyPage:
        
        company = paginator.page(paginator.num_pages)
   
    return render(request, 'store/international_company.html', {'factorys': company, 'count': count}) 

def lather(request):
    lather_companies = Company.objects.filter(type__name="lather")

    paginator = Paginator(lather_companies, 40) 
    page = request.GET.get('page')

    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
     
        companies = paginator.page(1)
    except EmptyPage:
       
        companies = paginator.page(paginator.num_pages)
    return render(request,'core/lather.html', {'companies': companies})


def synthetic(request):
    synthetic_companies = Company.objects.filter(type__name="synthetic")

    paginator = Paginator(synthetic_companies, 40)  
    page = request.GET.get('page')

    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
        
        companies = paginator.page(1)
    except EmptyPage:
        
        companies = paginator.page(paginator.num_pages)
    return render(request,'core/lather.html', {'companies': companies})

def esparadice(request):
    esparadice_companies = Company.objects.filter(type__name="esparadice")

    paginator = Paginator(esparadice_companies, 40) 
    page = request.GET.get('page')

    try:
        companies = paginator.page(page)
    except PageNotAnInteger:
   
        companies = paginator.page(1)
    except EmptyPage:
       
        companies = paginator.page(paginator.num_pages)
    return render(request,'core/lather.html', {'companies': companies})




def news_article_list(request):
    all_news = NewsArticle.objects.filter(is_availble=True).order_by('-publication_date')
    
    # Pagination for all news
    paginator = Paginator(all_news, 10)  # Assuming you want 10 news per page 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Splitting the news data into two parts
    num_news = len(all_news)
    mid_index = num_news // 2
    news_column1 = all_news[:mid_index]
    news_column2 = all_news[mid_index:]

    update_news = NewsArticle.objects.filter(is_availble=True).order_by('-publication_date')[:1]
    latest_news = NewsArticle.objects.filter(is_availble=True).order_by('-publication_date')[:3]  # Latest news won't be paginated

    context = {
        'news_column1': news_column1,
        'news_column2': news_column2,
        'page_obj': page_obj,
        'articles': update_news,
        'latest_news': latest_news,
    }

    return render(request, 'news/article_list.html', context)

def news_detail(request, news_slug):
    news = NewsArticle.objects.get(slug=news_slug)
    return render(request, 'news/news_details.html', {'news': news}) 

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event/event.html',{'events': events}) 

def event_detail(request, event_slug):
    event = Event.objects.get(slug=event_slug)
    return render(request, 'event/event_details.html', {'event': event})  


def gallery_list(request):
    galleries = Gallery.objects.prefetch_related('images', 'videos')
    return render(request, 'gallery/list.html', {'galleries': galleries}) 

def gallery_list(request):
    query = request.GET.get('q')  # Get the search term from the request
    if query:
        # Filter galleries based on the search term (case-insensitive)
        galleries = Gallery.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
        ).prefetch_related('images', 'videos')
    else:
        # Get all galleries if no search term is provided
        galleries = Gallery.objects.prefetch_related('images', 'videos')
    
    # Render the list.html template with galleries and the search query
    return render(request, 'gallery/list.html', {'galleries': galleries, 'query': query}) 

def leaders(request):
    leaders = Leaders.objects.all()
    return render(request, 'leader/leader.html', {'leaders': leaders})


def persion_detail(request, person_slug):
    leader = Leaders.objects.get(slug=person_slug)
    return render(request, 'leader/biography.html', {'leader': leader}) 



