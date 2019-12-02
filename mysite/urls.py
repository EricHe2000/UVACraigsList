"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic import TemplateView
from posts import views
from django.conf.urls.static import static
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('', views.mainIndex, name='index'),
  

    
    #Beginning of category links work-around
    
    path('electronics/', views.categoryElectronicsIndex, name='index'),
    path('services/', views.categoryServicesIndex, name='index'),
    path('misc/', views.categoryMiscellaneousIndex, name='index'),
    path('housing/', views.categoryHousingIndex, name='index'),
    path('food/', views.categoryFoodIndex, name='index'),
    path('community/', views.categoryCommunityIndex, name='index'),
    path('textbooks/', views.categoryTextbookIndex, name='index'),
    path('tutoring/', views.categoryTutoringIndex, name='index'),
    path('clothes/', views.categoryClothesIndex, name='index'),
    
    #End of category links work-around
    
    path('accounts/', include('allauth.urls')),
    path('profile/',include('login.urls')),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    path('',include('posts.urls')),
    url(r'^s3direct/', include('s3direct.urls')),
    ]
# ]  + static(mysite.settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

