from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.postIndex, name='posts'),
    path('newpost', views.addPost, name='newpost'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]