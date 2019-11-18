from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import UserProfile
# Create your tests here.
class ProfileTestCase(TestCase):
        def test_ProfileUpdateForm_valid(self):
                form = EditProfileForm(data={ 'email':'eriche2000@gmail.com ',
                                                'first_name':'Eric',
                                                'last_name':'He',
                                                })
                self.assertTrue(form.is_valid()) 

        def test_ProfileUpdateForm_invalid(self):
                form = EditProfileForm(data={ 'notemail':'eriche2000@gmail.com ',
                                                'first_name':'Eric',
                                                'last_name':'He',
                                                })
                self.assertTrue(form.is_valid()) 

        def test_ProfileUpdateForm_bound(self):
                form = EditProfileForm(data={ 'notemail':'eriche2000@gmail.com ',
                                                'first_name':'Eric',
                                                })
                self.assertTrue(form.is_valid()) 

        def test_ProfileUpdateForm_Badbound(self):
                form = EditProfileForm(data={  })
                self.assertTrue(form.is_valid()) 

        def test_ProfileUpdateForm_goodBound(self):
                form = EditProfileForm(data={  })
                self.assertTrue(form.is_valid())
                
class ProfileSetupModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create()

    def test_user_is_created(self):
        self.assertTrue(User.objects.count() == 1)
        

    def test_user_is_created2(self):
        self.user = User.objects.create()
        self.assertTrue(User.objects.count() == 2)

class UserProfileModelTest(TestCase):

    def test_profile_object(self):
       c = UserProfile(first_name="Eric", last_name="He")
       self.assertEqual(c.first_name, "Eric")
       self.assertEqual(c.last_name, "He")

    def test_profileUser_object(self):
       c = UserProfile(first_name="Eric", last_name="He")
       self.assertEqual(c.first_name, "Eric")
       self.assertEqual(c.last_name, "He")