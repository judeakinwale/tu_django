from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'transportation'

urlpatterns = [
    path("", views.TransportationListView.as_view(), name="transportation_list"),
    path("create/", views.TransportationCreateView.as_view(), name="transportation_create"),
    path("<pk>/", views.TransportationDetailView.as_view(), name="transportation_detail"),
    path("<pk>/update/", views.TransportationUpdateView.as_view(), name="transportation_update"),
    path("<pk>/delete/", views.TransportationDeleteView.as_view(), name="transportation_delete"),
]
