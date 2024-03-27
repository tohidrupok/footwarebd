from django.db import models

class Company(models.Model):
    company_name = models.CharField( max_length=100 )
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, unique = True)
    head_office_address = models.CharField(max_length=255)
    factory_addresses = models.TextField()  
    email_addresses = models.TextField() 
    phone_number = models.CharField(max_length=20, unique=True)
    managing_director_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/products', blank=True, null=True )
    logo = models.ImageField(upload_to='photos/logos',  default='photos/default.png')
    is_availble = models.BooleanField(default = True)
    website = models.URLField(max_length = 200, blank=True, null=True)    #website
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.company_name

    def generate_map_url(self):
        if self.latitude is not None and self.longitude is not None:
            return f"https://www.google.com/maps?q={self.latitude},{self.longitude}"
        else:
            return None

