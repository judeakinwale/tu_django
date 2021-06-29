from django import forms
from django.contrib.admin import widgets
from .models import Listing


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

        widgets = {
            'photo_main': widgets.AdminFileWidget(
                attrs={
                    'class': 'file w-100',
                    'data-browse-on-zone-click': 'true',
                })
        }

        help_texts = {
            'photo_main': 'Upload images with a 4:3 or 16:9 aspect ratio'
        }
