from django.contrib import admin
from . models import *

class companyadmin(admin.ModelAdmin): 
     list_display = ['company_name']
     
     prepopulated_fields = {'slug' : ('company_name',)}
     

class newsarticleadmin(admin.ModelAdmin): 
     list_display = ['title']
     
     prepopulated_fields = {'slug' : ('title',)}

     
admin.site.register(Company, companyadmin)
admin.site.register(NewsArticle, newsarticleadmin)

