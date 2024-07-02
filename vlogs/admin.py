from django.contrib import admin
from . models import *

class BlogAdmin(admin.ModelAdmin): 
     list_display = ['title']    
     prepopulated_fields = {'slug' : ('title',)} 

admin.site.register(Blog, BlogAdmin)
admin.site.register(Contact)
admin.site.register(Home)
admin.site.register(Video_HomePage)
admin.site.register(Management_Massage)
