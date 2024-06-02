from django.db import models
#Resource library
class Publication(models.Model):
    publication_date = models.DateField()
    name = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='publications/')

    def __str__(self):
        return self.name
#Supply Chain Info
class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length=200, unique=True)
    icon = models.ImageField(upload_to='category_icons/', default='photos/default.png', blank=True, null=True)  
    content = models.CharField(max_length = 500, blank=True, null=True)
   
    def __str__(self):
        return self.category_name 
    
class Company(models.Model):
    title = models.ForeignKey(Category, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    remark = models.TextField()

    def __str__(self):
        return self.title.category_name + ' - ' + self.company_name

#Certifications and Standards 

class Requirement(models.Model):
    title = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length=200, unique=True)
    icon = models.ImageField(upload_to='icon/', default='photos/default.png', blank=True, null=True)
    short_contant = models.CharField(max_length = 500, blank=True, null=True)
    contant = models.TextField()
    pdf_file = models.FileField(upload_to='certificates_category/', null=True, blank=True)

    def __str__(self):
        return self.title