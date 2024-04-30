from django.db import models
#Resource library
#
class Publication(models.Model):
    publication_date = models.DateField()
    name = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='publications/')

    def __str__(self):
        return self.name



#supply chain

class Category(models.Model):
    category_name = models.CharField(max_length = 50, unique = True)
    slug = models.SlugField(max_length=200, unique=True)
   
    def __str__(self):
        return self.category_name 
    

class Company(models.Model):
    serial_no = models.IntegerField(unique=True)
    title = models.ForeignKey(Category, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    remark = models.TextField()
    extra = models.CharField(max_length=100, null= True, blank= True)

    def __str__(self):
        return self.title.category_name + ' - ' + self.company_name
