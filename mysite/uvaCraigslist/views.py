from django.shortcuts import render
from django.http import HttpResponse
from .models import Category

def home(request):
    #return HttpResponse('If you can seeing this, Jake hasnt broken everything yet')
    categories = Category.objects.all()
    categories_names = list()

    for category in categories:
        categories_names.append(category.name)

    response_html = '<br>'.join(categories_names)

    return HttpResponse(response_html)
# Create your views here.
