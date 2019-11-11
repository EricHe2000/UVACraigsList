from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
import datetime
from .models import Photo

class PostForm(forms.Form):
    titleText = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    
    Electronics = 'Electronics'
    Services = 'Services'
    Miscellaneous = 'Misc'
    Housing = 'Housing'
    Food = 'Food'
    Community = 'Community'
    Textbooks = 'Textbooks'
    Tutoring = 'Tutoring'
    Clothes = 'Clothes'
    CategoryChoices = [
        (Miscellaneous, 'Miscellaneous'),
        (Electronics, 'Electronics'),
        (Services, 'Services'),
        (Housing, 'Housing'),
        (Food, 'Food'),
        (Community, 'Community'),
        (Textbooks, 'Textbooks'),
        (Tutoring, 'Tutoring'),
        (Clothes, 'Clothes'),
    ]
    category = forms.ChoiceField(choices=CategoryChoices)
    price = forms.DecimalField(max_digits=6, decimal_places=2)

    # model=Photo
    # fields=['title','photo']
    #Picture_Description=forms.CharField(max_length=200)
    #photo = forms.FileField()