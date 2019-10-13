from django.db import models

# Create your models here.

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.DO_NOTHING)
    #description = models.CharField(max_length=100, default='')
    address = models.CharField(max_length=100, default='')
    phone = models.IntegerField(default=0)
    image = models.ImageField(upload_to='profile_image', blank=True)
    email = models.CharField(max_length=100, default='')
   
    def __str__(self):
        return self.user.username

    def create_profile(sender, **kwargs):
	    if kwargs['created']:
	        user_profile = UserProfile.objects.create(user=kwargs['instance'])

#spost_save.connect(create_profile, sender=User)