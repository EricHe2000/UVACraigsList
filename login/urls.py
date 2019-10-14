from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from . import views


app_name = 'login'
urlpatterns= [
	path('', TemplateView.as_view(template_name='login/profile.html')),
	#path('/accounts/profile/', views.profile, name='profile' ),
]