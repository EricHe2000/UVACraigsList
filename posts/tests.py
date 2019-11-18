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

    def test_User_object5(self):
        user = User(username="ian",email="ijk8sw@virginia.edu")
        self.assertTrue(user.username, "lipin")
        self.assertTrue(user.email,"lip2eb@virginia.edu")

    def test_User_object6(self):
        user = User(username="ian",email="ijk8sw@virginia.edu")
        self.assertTrue(user.username, "lipin")
        self.assertTrue(user.email,"lip2eb@virginia.edu")

    def test_User_object7(self):
        user = User(username="ian",email="ijk8sw@virginia.edu")
        self.assertTrue(user.username, "lipin")
        self.assertTrue(user.email,"lip2eb@virginia.edu")

    def test_User_object8(self):
        user = User(username="ian",email="ijk8sw@virginia.edu")
        self.assertTrue(user.username, "lipin")
        self.assertTrue(user.email,"lip2eb@virginia.edu")

    def test_User_object9(self):
        user = User(username="ian",email="ijk8sw@virginia.edu")
        self.assertTrue(user.username, "lipin")
        self.assertTrue(user.email,"lip2eb@virginia.edu")

    def test_User_object10(self):
        user = User(username="ian",email="ijk8sw@virginia.edu")
        self.assertTrue(user.username, "lipin")
        self.assertTrue(user.email,"lip2eb@virginia.edu")

    def test_admin_page_status_code(self):
            response = self.client.get('/admin/')
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

    def Test_CommentForm_wrong1(self):
        form = CommentForm(data={})
        self.assertTrue(form.is_valid())

    def Test_CommentForm_wrong2(self):
        form = CommentForm(data={})
        self.assertTrue(form.is_valid())

    def Test_CommentForm_wrong3(self):
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
    
    def test_PostForm_true(self):
        form = PostForm(data={'titleText':"Bike",
                                'description':"Used Bike",
                                'category':'miscellaneous'})
        self.assertFalse(form.is_valid())

    def test_PostForm_false(self):
        form = PostForm(data={'titleText':"Bike",
                                'description':"Used Bike",
                                'category':'miscellaneous'})
        self.assertFalse(form.is_valid())