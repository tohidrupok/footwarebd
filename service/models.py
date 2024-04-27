from django.db import models

class Publication(models.Model):
    publication_date = models.DateField()
    name = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='publications/')

    def __str__(self):
        return self.name
