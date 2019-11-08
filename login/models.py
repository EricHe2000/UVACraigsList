from django.db import models
# Create your models here.

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete= models.DO_NOTHING)


   
    def __str__(self):
        return self.user.username


    @receiver(pre_save, sender=User)
    def update_username_from_email(sender, instance, **kwargs):
        instance.user = instance.email

