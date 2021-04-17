from django import forms
from django.contrib.admin import widgets
from .models import Transportation


class TransportationForm(forms.ModelForm):

    class Meta:
        model = Transportation
        fields = [
            'name',
            'description',
            'price',
            'phone',
            'capacity',
            'vehicle_type',
            'city',
            'state',
            'country',
            'photo_main',
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4',
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
