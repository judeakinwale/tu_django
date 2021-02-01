from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'cart'

urlpatterns = [
    path("", views.view_cart, name="view_cart"),
    path("delete/", views.delete_cart, name="delete_cart"),
    path("add/<slug>/", views.add_to_cart, name="add_to_cart"),
    path("remove/<slug>/", views.remove_from_cart, name="remove_from_cart"),
]
