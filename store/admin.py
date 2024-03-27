from django.contrib import admin
from . models import Company

class companyadmin(admin.ModelAdmin): 
     list_display = ['company_name', 'description', 'head_office_address', 'factory_addresses', 'email_addresses', 'phone_number', 'managing_director_name']
     
     prepopulated_fields = {'slug' : ('company_name',)}
     
admin.site.register(Company, companyadmin)