from django import forms
from django.contrib.admin import widgets
from .models import Listing, Realtor


class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        fields = [
            'title',
            'description',
            'price',
            'category',
            'bedrooms',
            'bathrooms',
            'pools',
            'lot_size',
            'street_address',
            'city',
            'state',
            'zipcode',
            'country',
            'photo_main',
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4',
            'photo_5',
            'photo_6',
        ]


class RealtorForm(forms.ModelForm):

    class Meta:
        model = Realtor
        fields = '__all__'
