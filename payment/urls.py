from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'payment'

urlpatterns = [
    # path(
    #     "payment/confirmation/",
    #     TemplateView.as_view(template_name='paystack/success-page.html'),
    #     name="payment_confirmation"
    #     ),
    path("payment/confirmation/", views.payment_confirmation, name="payment_confirmation"),
    path("checkout/", views.checkout, name="checkout"),
    path("checkout/<str:target>/<id>/", views.direct_checkout, name="direct_checkout"),
    path("pay/", TemplateView.as_view(template_name='payment/payment.html'), name="pay"),
    path("list-email/", views.event_creator_attendee_list_email, name="list_email"),
]
