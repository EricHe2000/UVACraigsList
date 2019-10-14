from django.apps import AppConfig
from django.db.models.signals import pre_save
from django.dispatch import receiver


class LoginConfig(AppConfig):
    name = 'login'

    def ready(self):
    	from django.contrib.auth.models import User
    	pre_save.connect(receiver,sender='login.UserProfile')
