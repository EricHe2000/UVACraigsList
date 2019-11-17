from django.test import TestCase
from django.contrib.auth.forms import UserCreationForm
from .forms import *

# Create your tests here.
def test_PrrofileUpdateForm_invalid(self):
        form = EditProfileForm(data={ 'email':'eriche2000@gmail.com ',
                                        'first_name':'Eric',
                                        'last_name':'He',
                                        })
        self.assertFalse(form.is_valid()) 