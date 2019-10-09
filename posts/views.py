from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Post
from django.http import HttpResponse
from django.utils import timezone


# Create your views here.
def index(request):
    posts_list = Post.objects.order_by('-creation_date')[:5]
    output = ', '.join([t.titleText for t in posts_list])
    return HttpResponse(output)

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(creation_date__lte=timezone.now())