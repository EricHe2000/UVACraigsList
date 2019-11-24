from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import logout
from django.conf import settings



app_name = 'login'

urlpatterns= [
    path('', views.view_profile, name='view_profile'),
	path('profileupdate', views.update_profile, name='profileupdate'),
	url(r'^profile/$', views.view_profile, name='view_profile'),
	path('logout', views.logout_view),
	path('posts/',include('posts.urls')),
	path('posts/newpost/',include('posts.urls')),
	
    ]