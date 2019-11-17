from django.urls import path
from django.conf.urls import url

from . import views
from .views import SearchResultsView
app_name = 'posts'
urlpatterns = [
    path('', views.postIndex, name='posts'),
    path('newpost', views.add_Post_view, name='newpost'),
    path('<int:num>/', views.PostDetailView, name='detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('posts', views.postIndex, name='posts'),
    
]