from django.contrib import admin
from . models import *

class companyadmin(admin.ModelAdmin): 
     list_display = ['company_name']
     
     prepopulated_fields = {'slug' : ('company_name',)}
     
admin.site.register(Company, companyadmin)
admin.site.register(NewsArticle)