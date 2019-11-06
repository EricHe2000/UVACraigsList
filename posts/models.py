from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    titleText = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now=True)
    
    Electronics = 'Electronics'
    Services = 'Services'
    Miscellaneous = 'Misc'
    CategoryChoices = [
        (Electronics, 'Electronics'),
        (Services, 'Services'),
        (Miscellaneous, 'Miscellaneous'),
    ]
    
    category = models.CharField(max_length=200, choices=CategoryChoices, default=Miscellaneous)
    
    price = models.DecimalField(max_digits=6, decimal_places=2)
    #https://djangopackages.org/packages/p/django-location-field/
    #user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.titleText
    
