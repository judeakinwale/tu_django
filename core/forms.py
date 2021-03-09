from django import forms
from django.contrib.admin import widgets
from django.utils.translation import gettext_lazy as _
from .models import Event, ContactUs


class EventForm(forms.ModelForm):
    start_time = forms.SplitDateTimeField(label='Start Date and Time', widget=widgets.AdminSplitDateTime())
    end_time = forms.SplitDateTimeField(label='End Date and Time', widget=widgets.AdminSplitDateTime())

    class Meta:
        model = Event
        fields = [
            'name',
            'image',
            'description',
            'category',
            'ticket_price',
            'ticket_sale_price',
            'street_address',
            'city',
            'state',
            'country',
            'start_time',
            'end_time',
            ]

        # labels = {
        #     'start_time': _('Start Date & Time'),
        #     'end_time': _('Start Date & Time'),
        # }

        widgets = {
            # 'start_time': widgets.AdminSplitDateTime(),
            # 'end_time': widgets.AdminSplitDateTime(),
            'image': widgets.AdminFileWidget(
                attrs={
                    'class': 'file w-100',
                    'data-browse-on-zone-click': 'true',
                })
        }

        # field_classes = {
        #     'slug': MySlugFormField,
        # }

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
