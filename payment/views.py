from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View
from .forms import CustomerInfoForm

from paystack.api.signals import payment_verified, event_signal
from django.dispatch import receiver


# Create your views here.

def customer_info(request):
    if request.method == "POST":
        customer_form = CustomerInfoForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return render(request, 'payment/payment.html', {'email':"human@jjj.co"})
        else:
            return HttpResponse('Invalid input try again!!!')
    else:
        customer_form = CustomerInfoForm()
    return render(request, 'payment/customer_info.html', {'customer_form': customer_form})


# Paystack Signals
@receiver(payment_verified)
def on_payment_verified(sender, ref,amount, **kwargs):
    """
    ref: paystack reference sent back.
    amount: amount in Naira.
    """
    pass


@receiver(event_signal)
def on_event_received(sender, event, data, **kwargs):
    # sender is the raw request
    # event is the event name that was passed https://developers.paystack.co/docs/events
    # data is the available data tied to the event
    pass
