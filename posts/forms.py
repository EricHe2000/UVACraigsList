from django import forms
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
import datetime
#from .models import Photo
from s3direct.widgets import S3DirectWidget

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
    file = forms.ImageField(required=False)
    #images = forms.URLField(widget=S3DirectWidget(dest='media'))




STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

#class PhotoForm(forms.form)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('email', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'address_1',
            'address_2',
            Row(
                Column('city', css_class='form-group col-md-6 mb-0'),
                Column('state', css_class='form-group col-md-4 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'check_me_out',
            Submit('submit', 'Sign in')
        )


class S3DirectUploadForm(forms.Form):
    images = forms.URLField(widget=S3DirectWidget(dest='example_destination'))
