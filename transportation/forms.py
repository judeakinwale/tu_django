from django import forms
from django.contrib.admin import widgets
from .models import Transportation, Operator


class TransportationForm(forms.ModelForm):

    class Meta:
        model = Transportation
        fields = [
            'name',
            'description',
            'price',
            'phone',
            'capacity',
            'category',
            'city',
            'state',
            'country',
            'photo_main',
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4',
        ]


class OperatorForm(forms.ModelForm):

    class Meta:
        model = Operator
        fields = '__all__'
