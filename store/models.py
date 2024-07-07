from django.db import models

class type(models.Model):
    name = models.CharField(max_length= 100) 
    def __str__(self):
        return self.name
    
class Company(models.Model):
    company_name = models.CharField( max_length=100 )
    type = models.ForeignKey(type, on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500)
    head_office_address = models.CharField(max_length=255)
    factory_addresses = models.TextField()  
    email_addresses = models.TextField() 
    phone_number = models.CharField(max_length=100, unique=True)
    managing_director_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/products', blank=True, null=True )
    logo = models.ImageField(upload_to='photos/logos',  default='photos/default.png')
    is_availble = models.CharField( max_length=100 )
    website = models.URLField(max_length = 200, blank=True, null=True)   
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.company_name

    def generate_map_url(self):
        if self.latitude is not None and self.longitude is not None:
            return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"
        else:
            return None 


class Factory(models.Model):
    factory_name = models.CharField(max_length=60)
    owner_name = models.CharField(max_length=60)
    responsibility = models.CharField(max_length=30)
    address = models.CharField(max_length=155)
    contact = models.CharField(max_length=50)
    product = models.CharField(max_length=60)
    Extra = models.CharField(max_length=100)

    def __str__(self):
        return self.factory_name
  
  
class InternationaCompany(models.Model):
    company_name = models.CharField(max_length=60)
    owner_name = models.CharField(max_length=60)
    responsibility = models.CharField(max_length=30)
    address = models.CharField(max_length=155)
    contact = models.CharField(max_length=50)
    product = models.CharField(max_length=60)
    Extra = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name 
    

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, blank=True, null=True)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/news_images/', null=True, blank=True)
    is_availble = models.BooleanField(default = True)
    reference_link = models.URLField(max_length = 200, blank=True, null=True)  

    def __str__(self):
        return self.title 
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True)
    content = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    social_link = models.URLField(max_length = 200, blank=True, null=True)  
    image1 = models.ImageField(upload_to='photos/events_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='photos/events_images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='photos/events_images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='photos/events_images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='photos/events_images/', null=True, blank=True)
    image6 = models.ImageField(upload_to='photos/events_images/', null=True, blank=True)


    def __str__(self):
        return self.title 
    
# Gallery start

class Gallery(models.Model):
    title = models.CharField(max_length=200, help_text='Title of the gallery')
    description = models.TextField(blank=True, help_text='Description of the gallery')

    def __str__(self):
        return self.title

class Image(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='gallery/images2/', null=True, blank=True)
    image3 = models.ImageField(upload_to='gallery/images3/', null=True, blank=True)

    def __str__(self):
        return f"Image in {self.gallery.title}"

class Video(models.Model):
    gallery = models.ForeignKey(Gallery, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='gallery/videos/')
    video2 = models.FileField(upload_to='gallery/videos2/', null=True, blank=True)

    def __str__(self):
        return f"Video in {self.gallery.title}"
 


class Leaders(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    title = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)
    nationality = models.CharField(max_length=100)
    education = models.TextField()
    description = models.TextField()
    professional_history = models.TextField(blank=True, null=True)
    business_history = models.TextField(blank=True, null=True)
    achievement = models.TextField(blank=True, null=True)
    awards = models.TextField(blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    role_in_industries = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='leader_images/', blank=True, null=True)
    facebook = models.CharField(max_length=200, blank=True, null=True)  
    linkedin = models.CharField(max_length=200, blank=True, null=True)  
    website = models.URLField(max_length=200, blank=True, null=True) 
      
      
    def __str__(self):
        return self.name

