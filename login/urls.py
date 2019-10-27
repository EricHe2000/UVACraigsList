from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView
from . import views
from django.contrib.auth import logout
from django.conf import settings



app_name = 'login'
urlpatterns= [
	path('', TemplateView.as_view(template_name='posts/index.html')),
	path('logout', logout, {'next_page': settings.LOGOUT_REDIRECT_URL},name='logout'),
	

    ]