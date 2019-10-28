from django import forms


class listingForm(forms.Form):
    titleText = forms.CharField(max_length=200)
    description = forms.CharField(max_length=200)
    creation_date = forms.CharField(max_length=200)
    postID = forms.IntegerField()
    category = forms.CharField(max_length=200)
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    #https://djangopackages.org/packages/p/django-location-field/

    