from django import forms
from django.contrib.admin import widgets
from .models import Transportation, Operator


class TransportationForm(forms.ModelForm):

    class Meta:
        model = Transportation
        fields = '__all__'


class OperatorForm(forms.ModelForm):

    class Meta:
        model = Operator
        fields = '__all__'
