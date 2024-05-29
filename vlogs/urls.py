from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.logo_animation, name="logo"),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:blog_slug>/', views.blog_detail, name='blog_details'),
    path('contact/', views.contact_view, name='contact'),

] 



