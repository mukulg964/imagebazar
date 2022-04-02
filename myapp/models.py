from distutils.command import upload
from django.db import models

# Create your models here.
class category(models.Model):
    title =models.CharField(max_length=100)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title



class images(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    date = models.TimeField()
    cat = models.ForeignKey(category,on_delete=models.CASCADE)

    def __str__(self):
        return self.title