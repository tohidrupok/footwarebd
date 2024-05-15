from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Company, NewsArticle, Leaders , Factory

def company_list(request):
    all_companies = Company.objects.filter(is_availble=True)

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


def leaders(request):
    leaders = Leaders.objects.all()
    return render(request, 'leader/leader.html', {'leaders': leaders})


def persion_detail(request, person_slug):
    leader = Leaders.objects.get(slug=person_slug)
    return render(request, 'leader/biography.html', {'leader': leader}) 



