from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Post
from django.http import HttpResponse
from django.utils import timezone


#Citations
# http://www.learningaboutelectronics.com/Articles/How-to-insert-data-into-a-database-from-an-HTML-form-in-Django.php


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
'''
def newPost(request):

    #template_name = 'posts/index.html'
    postList = Post.objects.order_by('-creation_date')[:3]
    testArray = {1, 2, 3} 
 
    context = {'postList': postList, 'testArray': testArray}
    
    return render(request, 'posts/newPost.html', context)

'''
def newPostTest(request):

    post=Post()
    post.titleText = "test"
    post.description = "test"
    post.creation_date = "2006-10-25"
    postID = 5
    category="test"
    post.save()

    if request.method == 'POST':
        post=Post()
        post.titleText=request.POST['titleText']
        post.description=request.POST['description']
        post.creation_date=request.POST['creation_date']
        post.postID=request.POST['postID']
        post.category=request.POST['category']
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

'''
def Post(request):
    
    
    selected_choice = request.POST['choice']
    
    post.Post();
    
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
'''
class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Post.objects.filter(creation_date__lte=timezone.now())
        
class PostCreate(generic.CreateView):
    template_name = 'posts/newPost.html'
    model = Post
    fields = '__all__'

    def form_valid(self, form):
        model = form.save(commit=False)
        model.save()
        return redirect('/posts')