from django.urls import path
from . import views

urlpatterns = [
    path('job/', views.job_list, name='job_list'),
    path('submit_resume/<int:job_id>/', views.submit_resume, name='submit_resume'),
]
