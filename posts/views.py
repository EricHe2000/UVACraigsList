from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Post
from django.http import HttpResponse
from django.utils import timezone


# Create your views here.
'''
def index(request):
    posts_list = Post.objects.order_by('-creation_date')[:5]
    output = ', '.join([t.titleText for t in posts_list])
    return HttpResponse(output)
'''
'''
class IndexView(generic.ListView):
    template_name = 'posts/index.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        #This returns the most recent posts
        
        return Post.objects.order_by('-creation_date')[:3]
'''
def index(request):

    #template_name = 'posts/index.html'
    postList = Post.objects.order_by('-creation_date')[:3]
    testArray = {1, 2, 3} 
 
    context = {'postList': postList, 'testArray': testArray}
    
    return render(request, 'posts/index.html', context)
 

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(creation_date__lte=timezone.now())