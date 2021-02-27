from django import forms
from django.contrib.admin import widgets
from .models import Event


class EventForm(forms.ModelForm):
    start_time = forms.SplitDateTimeField(label='Start Date and Time', widget=widgets.AdminSplitDateTime())
    end_time = forms.SplitDateTimeField(label='End Date and Time', widget=widgets.AdminSplitDateTime())  

    class Meta:
        model = Event
        fields = [  'name', 
                    'image', 
                    'description', 
                    'category', 
                    'price', 
                    'sale_price', 
                    'location', 
                    'city', 
                    'state', 
                    'country', 
                    'start_time', 
                    'end_time', 
                    'active',]

        # widgets = {
        #     'start_time': widgets.AdminSplitDateTime(),
        #     'end_time': widgets.AdminSplitDateTime(),
        # }
        # field_classes = {
        #     'slug': MySlugFormField,
        # }