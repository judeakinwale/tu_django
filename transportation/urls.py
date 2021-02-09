from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'transportation'

urlpatterns = [
    path("listings/", views.TransportationListView.as_view(), name="transportation_list"),
    path("listing/<pk>/", views.TransportationDetailView.as_view(), name="transportation_detail"),
]
