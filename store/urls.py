from django.urls import path
from . import views

urlpatterns = [
    path('company/', views.company_list ,name='company_list'),
    # path('product_detail/<slug:product_slug>/', views.product_detail ,name='product_detail'),
    path('company/<slug:company_slug>/', views.company_detail ,name='company_detail'),
    path('news/', views.news_article_list ,name='news_all'),
    path('leaders/', views.leaders ,name='leaders'),
    path('leaders/<slug:person_slug>/', views.persion_detail ,name='person_detail'),
    
]