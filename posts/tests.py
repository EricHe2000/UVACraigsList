import datetime
from django.test import TestCase
from django.utils import timezone
from django.db import models

from .models import Post

''' 
class PostModelTests(TestCase):
    
    def test_posted_recently(self):
    
        #postVar = Post.objects.order_by('-creation_date')[:3]

        time = timezone.now() + datetime.timedelta(days=30)
    
        future_post = Post(creation_date=time)
    
        self.assertIs(future_post.was_published_recently(), False) """

# Create your tests here.

'''
'''
    titleText = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    creation_date = models.CharField(max_length=200)
    postID = models.IntegerField()
    category = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)

'''

class PostTestCase(TestCase):
    def setUp(self):
    
        Post.objects.create(titleText="testCase", 
                            description="testCase", 
                            creation_date="2019-10-31",
                            category="testCase",
                            price=2.00)
        
    def test_post_created(self):
            
        #Checks if post can be created and added to the database
        
        testCaseObject = Post.objects.get(titleText="testCase")
            
        self.assertEqual(testCaseObject.titleText,"testCase")
        
    def test_unique_ID(self):
    
        #Checks if each post has its own unique ID
        totalPostsInDatabase = 5
    
        postList = Post.objects.order_by('-creation_date')[:totalPostsInDatabase]
        
        postIDRepeatBool = 0
        
        for count1 in postList:
            for count2 in postList:
                if (count1.id == count2.id):
                    postIDRepeatBool = 1
        
        self.assertEqual(postIDRepeatBool, 1)
        
    def test_no_negative_prices(self):
    
        postPriceNegativeBool = 0
    
        totalPostsInDatabase = 5
    
        postList = Post.objects.order_by('-creation_date')[:totalPostsInDatabase]
        
        for count1 in postList:
            if(count1.price <= 0):
                postPriceNegativeBool = 1
                            
        self.assertEqual(postPriceNegativeBool, 0);
        
    def test_no_blank_titleText(self):
    
        totalPostsInDatabase = 5
        
        postTitleTextBlankBool = 0
        
        postList = Post.objects.order_by('-creation_date')[:totalPostsInDatabase]
        
        for count1 in postList:
            if(count1.titleText == ""):
                postTitleTextBlankBool = 1
                
        self.assertEqual(postTitleTextBlankBool, 0);
        
    def test_no_blank_description(self):
    
        totalPostsInDatabase = 5
        
        postDescriptionBlankBool = 0
        
        postList = Post.objects.order_by('-creation_date')[:totalPostsInDatabase]
        
        for count1 in postList:
            if(count1.description == ""):
                postDescriptionBlankBool = 1
                
        self.assertEqual(postDescriptionBlankBool, 0);
        