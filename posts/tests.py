import datetime
from django.test import TestCase
from django.utils import timezone
from django.db import models

from .models import Post

class PostModelTests(TestCase):
    
    def test_posted_recently(self):
    
        #postVar = Post.objects.order_by('-creation_date')[:3]

        time = timezone.now() + datetime.timedelta(days=30)
    
        future_post = Post(creation_date=time)
    
        self.assertIs(future_post.was_published_recently(), True)

# Create your tests here.
