from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.index, name='index'),
    #path('', views.IndexView.as_view(), name='index'),
    path('newPost/', views.newPost, name='newPost'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]