from django.contrib import admin
from . models import *

class companyadmin(admin.ModelAdmin): 
     list_display = ['company_name']    
     prepopulated_fields = {'slug' : ('company_name',)}
     
class newsarticleadmin(admin.ModelAdmin): 
     list_display = ['title']    
     prepopulated_fields = {'slug' : ('title',)} 

class Leadersadmin(admin.ModelAdmin): 
     list_display = ['name']    
     prepopulated_fields = {'slug' : ('name',)}

     
admin.site.register(Company, companyadmin)
admin.site.register(NewsArticle, newsarticleadmin)
admin.site.register(Leaders, Leadersadmin)

