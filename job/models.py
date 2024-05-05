from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)  
    company = models.CharField(max_length=100, blank=True, null= True)
    deadline = models.DateField( blank=True, null= True)
    link = models.URLField( blank=True, null= True)
    # Add any other fields you need for a job

class Resume(models.Model):
    job = models.ForeignKey(Job, related_name='resumes', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    submitted_at = models.DateTimeField(auto_now_add=True)
