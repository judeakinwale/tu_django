from django import forms
from django.contrib.admin import widgets
from django.utils.translation import gettext_lazy as _
from .models import Event, ContactUs


class EventForm(forms.ModelForm):
    start_time = forms.SplitDateTimeField(label='Start Date and Time', widget=widgets.AdminSplitDateTime(attrs={
        'class': 'form-control'
    }))
    end_time = forms.SplitDateTimeField(label='End Date and Time', widget=widgets.AdminSplitDateTime(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = Event
        fields = [
            'name',
            'description',
            'image',
            'category',
            'ticket_price',
            'ticket_sale_price',
            'ticket_quantity',
            'street_address',
            'city',
            'state',
            'country',
            'start_time',
            'end_time',
        ]

        widgets = {
            'image': widgets.AdminFileWidget(
                attrs={
                    'class': 'file w-100',
                    'data-browse-on-zone-click': 'true',
                })
        }

        help_texts = {
            'image': 'Upload images with a 4:3 or 16:9 aspect ratio'
        }


class ContactUsForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = '__all__'

        widgets = {
            'email': widgets.AdminEmailInputWidget(attrs={
                'placeholder': 'user@example.com'
            }),
            'message' : widgets.AdminTextareaWidget(attrs={
                'placeholder': "Write your notes or questions here..."
            }),
        }

    # TODO: Define form fields here
