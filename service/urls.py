from django.urls import path
from . import views

urlpatterns = [
    path('resource_library/', views.publications_list, name='resource_library'),
    path('resource_library/<int:publication_id>/download/', views.download_pdf, name='download_pdf'),
    path('supply_chain/', views.supply_chain, name='supply_chain'),
    path('supply_chain/<slug:category_slug>/', views.category, name='category_list'),
]

