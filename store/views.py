from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Company, NewsArticle

def company_list(request):
    all_companies = Company.objects.filter(is_availble=True)

    paginator = Paginator(all_companies, 2)  # 10 companies per page
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
    return render(request, 'store/company_detail.html', context) 

def news_article_list(request):
    general_news = NewsArticle.objects.filter(is_availble=True)
    
    paginator = Paginator(general_news, 1)  # 10 articles per page
    page = request.GET.get('page')

    try:
        general_news = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        general_news = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        general_news = paginator.page(paginator.num_pages)
    articles = NewsArticle.objects.filter(is_availble=True).order_by('-publication_date')[:1]
    latest_news = NewsArticle.objects.filter(is_availble=True).order_by('-publication_date')[:6]  # Latest news won't be paginated

    context = {'articles': articles, 'latest_news': latest_news,'general_news': general_news }
    return render(request, 'news/article_list.html', context)

