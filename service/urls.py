from django.urls import path
from . import views

urlpatterns = [
    path('resource_library/', views.publications_list, name='resource_library'),
    path('resource_library/<int:publication_id>/download/', views.download_pdf, name='download_pdf'),
]
