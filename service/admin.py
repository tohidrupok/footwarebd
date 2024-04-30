from django.contrib import admin
from .models import Publication, Category, Company

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'publication_date')
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin): 
    list_display = ['category_name']     
    prepopulated_fields = {'slug': ('category_name',)}  # Note the tuple ('category_name',)

admin.site.register(Publication, PublicationAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Company)
