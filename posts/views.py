from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Post, Photo
from django.http import HttpResponse
from django.utils import timezone
from .forms import PostForm 
import operator

from django.db.models import Q


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

def addPost(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            data = request.POST.copy()
            p3 = Photo(photo=data.get('photo'))
            p3.save()
            post = Post(
                titleText = data.get('titleText'), 
                description=data.get('description'), 
                creation_date = data.get('creation_date'), 
                category = data.get('category'), 
                price = data.get('price'), 
                upload = p3,
                )
            post.save()
            # redirect to a new URL:
            return HttpResponseRedirect('/posts')

        # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

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
        



class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(titleText__icontains=query) | Q(category__icontains=query)
        )
        return object_list