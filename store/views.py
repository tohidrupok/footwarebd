from django.shortcuts import render
from .models import Company

def company_list(request):
    companies = Company.objects.filter(is_availble=True)
    return render(request, 'store/company_list.html', {'companies': companies})

def company_detail(request, company_slug):
    company = Company.objects.get(slug=company_slug)
    map_url = company.generate_map_url()
    context = {
        'company': company,
        'map_url': map_url
    }
    return render(request, 'store/company_detail.html', context)
