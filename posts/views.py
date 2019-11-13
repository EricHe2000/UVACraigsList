from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import *
from django.http import HttpResponse
from django.utils import timezone
from .forms import *
import operator
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.core.files.storage import default_storage
import boto3
from django.conf import settings
import os




#Citations
# http://www.learningaboutelectronics.com/Articles/How-to-insert-data-into-a-database-from-an-HTML-form-in-Django.php


# Create your views here.
    

def postIndex(request):
    
    template_name = 'posts/postIndex.html'
    postList = Post.objects.order_by('-creation_date')
    categoryClicked = 'all'
    context = {'postList': postList, 'categoryClicked': categoryClicked} 
    return render(request, 'posts/postIndex.html',context)  
    
def mainIndex(request):
    
    template_name = 'posts/index.html'
    postList = Post.objects.order_by('-creation_date')
    categoryClicked = 'all'
    context = {'postList': postList, 'categoryClicked': categoryClicked} 
    return render(request, 'posts/index.html',context)  

'''
Beginning of category indexs
'''

def categoryElectronicsIndex(request):
    
    template_name = 'posts/postIndex.html'
    postList = Post.objects.order_by('-creation_date')
    categoryClicked = 'Electronics'
    context = {'postList': postList, 'categoryClicked': categoryClicked} 
    return render(request, 'posts/postIndex.html',context)  

def categoryServicesIndex(request):
    
    template_name = 'posts/postIndex.html'
    postList = Post.objects.order_by('-creation_date')
    categoryClicked = 'Services'
    context = {'postList': postList, 'categoryClicked': categoryClicked} 
    return render(request, 'posts/postIndex.html',context)  

def categoryMiscellaneousIndex(request):
    
    template_name = 'posts/postIndex.html'
    postList = Post.objects.order_by('-creation_date')
    categoryClicked = 'Miscellaneous'
    context = {'postList': postList, 'categoryClicked': categoryClicked} 
    return render(request, 'posts/postIndex.html',context)  

def categoryHousingIndex(request):
    
    template_name = 'posts/postIndex.html'
    postList = Post.objects.order_by('-creation_date')
    categoryClicked = 'Housing'
    context = {'postList': postList, 'categoryClicked': categoryClicked} 
    return render(request, 'posts/postIndex.html',context)  

def categoryFoodIndex(request):
    
    template_name = 'posts/postIndex.html'
    postList = Post.objects.order_by('-creation_date')
    categoryClicked = 'Food'
    context = {'postList': postList, 'categoryClicked': categoryClicked} 
    return render(request, 'posts/postIndex.html',context)  

def categoryCommunityIndex(request):
    
    template_name = 'posts/postIndex.html'
    postList = Post.objects.order_by('-creation_date')
    categoryClicked = 'Community'
    context = {'postList': postList, 'categoryClicked': categoryClicked} 
    return render(request, 'posts/postIndex.html',context)  

def categoryTextbookIndex(request):
    
    template_name = 'posts/postIndex.html'
    postList = Post.objects.order_by('-creation_date')
    categoryClicked = 'Textbooks'
    context = {'postList': postList, 'categoryClicked': categoryClicked} 
    return render(request, 'posts/postIndex.html',context)  

def categoryTutoringIndex(request):
    
    template_name = 'posts/postIndex.html'
    postList = Post.objects.order_by('-creation_date')
    categoryClicked = 'Tutoring'
    context = {'postList': postList, 'categoryClicked': categoryClicked} 
    return render(request, 'posts/postIndex.html',context)  
    
def categoryClothesIndex(request):
    
    template_name = 'posts/postIndex.html'
    postList = Post.objects.order_by('-creation_date')
    categoryClicked = 'Clothes'
    context = {'postList': postList, 'categoryClicked': categoryClicked} 
    return render(request, 'posts/postIndex.html',context)  

'''
End of category indexes
'''

def add_Post_view(request):
    if request.method == 'POST':
        form=PostForm(request.POST,request.FILES)
        # print (PostForm())
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/posts')
    else:
        form=PostForm()
    return render(request, 'posts/newpost.html', {'form': form})



def detail(request, post_id):

    return HttpResponse("You're looking at question %s." % post_id)

def newPostTest(request):

    post=Post()
    post.titleText = "test"
    post.description = "test"
    post.creation_date = "2006-10-25"
    post.category="test"
    post.save()

    if request.method == 'POST':
        post=Post()
        post.titleText=request.POST['titleText']
        post.description=request.POST['description']
        post.creation_date=request.POST['creation_date']
        post.category=request.POST['category']
        post.upload=request.POST['photo']
        post.save()
        
        '''
        titleText = request.POST['titleText']
        description = request.POST['description']
        
        post = Post.objects.create(
            titleText = titleText,
            description = description
        )
        '''
        return render(request, 'posts/index.html')  

    else:
            return render(request,'posts/index.html')


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    
    def get_queryset(self):
        return Post.objects.filter(creation_date__lte=timezone.now())
        

# class CreatePostView(generic.FormView):
#     form_class=PostForm
#     template_name='posts/newpost.html'
#     success_url='../posts'


class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(titleText__icontains=query) | Q(category__icontains=query)
        )
        return object_list