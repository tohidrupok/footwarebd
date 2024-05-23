from django.contrib import admin
from . models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin): 
     list_display = ['title']    
     prepopulated_fields = {'slug' : ('title',)} 


admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)
