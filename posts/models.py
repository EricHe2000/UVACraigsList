from django.db import models
from django.utils import timezone
import datetime
import uuid
from django.contrib.auth.models import User
from s3direct.fields import S3DirectField
Default_id=1


class Photo(models.Model):
    # uuid = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False,
    #     )
    created_at = models.DateTimeField(auto_now_add=True) 
    file = models.FileField()
    #image = S3DirectField(dest='media')


# Create your models here.
class Post(models.Model):
    titleText = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    creation_date = models.DateTimeField(auto_now=True)
    
    Electronics = 'Electronics'
    Services = 'Services'
    Miscellaneous = 'Misc'
    Housing = 'Housing'
    Food = 'Food'
    Community = 'Community'
    Textbooks = 'Textbooks'
    Tutoring = 'Tutoring'
    Clothes = 'Clothes'
    CategoryChoices = [
    (Electronics, 'Electronics'),
    (Services, 'Services'),
    (Miscellaneous, 'Miscellaneous'),
    (Housing, 'Housing'),
    (Food, 'Food'),
    (Community, 'Community'),
    (Textbooks, 'Textbooks'),
    (Tutoring, 'Tutoring'),
    (Clothes, 'Clothes'),
    ]
    category = models.CharField(max_length=200, choices=CategoryChoices, default=Miscellaneous)
    
    price = models.DecimalField(max_digits=6, decimal_places=2)
    #https://djangopackages.org/packages/p/django-location-field/
    # user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=Default_id)
    upload = models.OneToOneField(Photo,on_delete=models.DO_NOTHING)


    def __str__(self):
        return self.titleText

