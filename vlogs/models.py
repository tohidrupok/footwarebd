from django.db import models

class Home(models.Model):
    slide = models.ImageField(upload_to='photos/slide/')
    big_text = models.CharField(max_length=70, null=True, blank=True)
    small_text = models.CharField(max_length=120, null=True, blank=True)
    
class Video_HomePage(models.Model):
    video = models.FileField(upload_to='videos/Slide Video')  

class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True, null=True)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/blog_images/', null=True, blank=True)
    reference_link = models.URLField(max_length = 200, blank=True, null=True)  

    def __str__(self):
        return self.title 


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
        

    
        

