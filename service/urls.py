from django.urls import path
from . import views

urlpatterns = [
    path('resource_library/', views.publications_list, name='resource_library'),
    path('resource_library/<int:publication_id>/', views.publications_list, name='download_pdf'),

    path('supply_chain/', views.supply_chain, name='supply_chain'),
    path('supply_chain/<slug:category_slug>/', views.category, name='category_list'),

    path('certifications_standards/', views.certifications_requirement_list, name='requirement_list'),
    path('certifications_standards/<slug:requirement_slug>/', views.requirements_detail, name='requirement'),
]

