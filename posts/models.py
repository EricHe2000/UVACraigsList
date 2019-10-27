from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
class Post(models.Model):
    titleText = models.CharField(max_length=200)
    description = models.TextField()
    creation_date = models.TextField()
    postID = models.IntegerField()
    category = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    #https://djangopackages.org/packages/p/django-location-field/

    def __str__(self):
        return self.titleText
    
