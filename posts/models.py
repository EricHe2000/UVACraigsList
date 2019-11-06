from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

Default_id=1

# Create your models here.
class Post(models.Model):
    titleText = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    #https://djangopackages.org/packages/p/django-location-field/
    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    User = models.ForeignKey(User, on_delete=models.CASCADE, default=Default_id)

    def __str__(self):
        return self.titleText
    
