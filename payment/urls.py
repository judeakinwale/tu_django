from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'payment'

urlpatterns = [
    path("payment-confirmation/", TemplateView.as_view(template_name='core/payment_confirmation.html'), name="payment_confirmation"),
    path("checkout/", TemplateView.as_view(template_name='core/checkout.html'), name="checkout"),
    path("contact/", TemplateView.as_view(template_name='core/contact_us.html'), name="contact_us"),
    path("customer_info/", views.customer_info, name="customer_info"),
]
