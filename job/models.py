from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)  
    description = models.CharField(max_length=300, blank=True, null= True)  
    company = models.CharField(max_length=100, blank=True, null= True)
    deadline = models.DateField( blank=True, null= True)
    experience = models.CharField(max_length=100, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    responsibility = models.TextField(blank=True, null=True)
    skills_required = models.CharField(max_length=100, blank=True, null=True)    
    salary = models.CharField(max_length=100, blank=True, null=True)  
    duration = models.CharField(max_length=100, blank=True, null=True)
    others_facility = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.title
    

class Resume(models.Model):
    job = models.ForeignKey(Job, related_name='resumes', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resumes/')
    submitted_at = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50,blank=True, null=True)
    experience = models.IntegerField(blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    contact = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    expected_salary = models.CharField(max_length=50, blank=True, null=True)
    remark = models.TextField(blank=True, null=True)


    def __str__(self):
        return f"{self.job.title} --- {self.name} --- Experience: {self.experience} Years --- Apply Date: {self.submitted_at}"

    
    
    