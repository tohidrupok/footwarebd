from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_list ,name='company_list'),
    # path('product_detail/<slug:product_slug>/', views.product_detail ,name='product_detail'),
    path('company_detail/<slug:company_slug>/', views.company_detail ,name='company_detail'),
    
]