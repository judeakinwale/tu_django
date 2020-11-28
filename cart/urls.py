from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'cart'

urlpatterns = [
    path("cart/", views.view_cart, name="view_cart"),
    path("cart/<slug>/", views.add_to_cart, name="add_to_cart"),
    path("cart/<id>/", views.remove_from_cart, name="remove_from_cart"),
]
