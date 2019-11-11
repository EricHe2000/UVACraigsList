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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    path('', views.mainIndex, name='index'),
  

    
    #Beginning of category links work-around
    
    path('category/electronics/', views.categoryElectronicsIndex, name='index'),
    path('category/services/', views.categoryServicesIndex, name='index'),
    path('category/misc/', views.categoryMiscellaneousIndex, name='index'),
    path('category/housing/', views.categoryHousingIndex, name='index'),
    path('category/food/', views.categoryFoodIndex, name='index'),
    path('category/community/', views.categoryCommunityIndex, name='index'),
    path('category/textbooks/', views.categoryTextbookIndex, name='index'),
    path('category/tutoring/', views.categoryTutoringIndex, name='index'),
    path('category/clothes/', views.categoryClothesIndex, name='index'),
    
    #End of category links work-around
    
    path('accounts/', include('allauth.urls')),
    path('profile/',include('login.urls')),
    url(r'^auth/', include('social_django.urls', namespace='social')),
    path('',include('posts.urls')),
    url(r'^s3direct/', include('s3direct.urls')),
    ]
# ]  + static(mysite.settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
