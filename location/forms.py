from django import forms
from django.contrib.admin import widgets
from .models import Listing, Realtor


class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = '__all__'


class RealtorForm(forms.ModelForm):

    class Meta:
        model = Realtor
        fields = '__all__'
