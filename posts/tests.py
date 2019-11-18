import datetime
from django.test import TestCase
from django.utils import timezone
from django.db import models
from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse
from .models import Post
from .forms import *

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
        
    def test_post_createdPrice(self):
            
        #Checks if post can be created and added to the database
        
        testCaseObject = Post.objects.get(price="11")
            
        self.assertEqual(testCaseObject.price,"11")

    def test_post_createdDescription(self):
            
        #Checks if post can be created and added to the database
        
        testCaseObject = Post.objects.get(description="11")
            
        self.assertEqual(testCaseObject.description,"11")

    def test_post_createdCategory(self):
            
        #Checks if post can be created and added to the database
        
        testCaseObject = Post.objects.get(category="miscellaneous")
            
        self.assertEqual(testCaseObject.category,"miscellaneous")

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

    def test_blank(self):
    
        totalPostsInDatabase = 5
        
        postDescriptionBlankBool = 0
        
        postList = Post.objects.order_by('-creation_date')[:totalPostsInDatabase]
        
        for count1 in postList:
            if(count1.description == ""):
                postDescriptionBlankBool = 1
                
        self.assertEqual(postDescriptionBlankBool, 0);

class DefaultUserModelTest(TestCase):

    def test_User_object(self):
        user = User(username="eric",email="eh4xv@virginia.edu")
        self.assertEqual(user.username, "eric")
        self.assertEqual(user.email,"eh4xv@virginia.edu")

    def test_User_object1(self):
        user = User(username="joseph",email="jsl8wv@virginia.edu")
        self.assertEqual(user.username, "joseph")
        self.assertEqual(user.email,"jsl8wv@virginia.edu")

    def test_User_object3(self):
        user = User(username="lipin",email="lip2eb@virginia.edu")
        self.assertEqual(user.username, "lipin")
        self.assertEqual(user.email,"lip2eb@virginia.edu")

    def test_User_object4(self):
        user = User(username="ian",email="ijk8sw@virginia.edu")
        self.assertTrue(user.username, "lipin")
        self.assertTrue(user.email,"lip2eb@virginia.edu")

class ViewTest(TestCase):
    def test_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
    
    def test_register_page_status_code(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)

    def test_profile_page_status_code(self):
        response = self.client.get(reverse('profile'))
        self.assertEquals(response.status_code, 302)

    def test_admin_page_status_code(self):
            response = self.client.get('/admin/')
            self.assertEquals(response.status_code, 302)

    def test_search_results_page_status_code(self):
        response = self.client.get(reverse('profiles:users'))
        self.assertEquals(response.status_code, 302)

class Comment_Form_Test(TestCase):

    def test_CommentForm_valid(self):
        form = CommentForm(data={
        'body':"I would love to buy"
        })
        self.assertFalse(form.is_valid())

    def test_CommentForm_correct(self):
        form = CommentForm(data={
        'body':"random"
        })
        self.assertFalse(form.is_valid())

    def Test_CommentForm_invalid(self):
        form = CommentForm(data={})
        self.assertTrue(form.is_valid())

    def Test_CommentForm_wrong(self):
        form = CommentForm(data={})
        self.assertTrue(form.is_valid())

class Post_Form_Test(TestCase):

    def test_PostForm_valid(self):
        form = PostForm(data={'titleText':"Bike",
                                'description':"Used Bike",
                                'category':'miscellaneous',
                                'price':"11",
                                'file':"hello.jpg"})
        self.assertFalse(form.is_valid())

    def test_PostForm_invalid(self):
        form = PostForm(data={'titleText':"Bike",
                                'description':"Used Bike",
                                'category':'miscellaneous'})
        self.assertFalse(form.is_valid())