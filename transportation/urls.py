from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'transportation'

urlpatterns = [
    path("listings/", views.TransportationListView.as_view(), name="transportation_list"),
    path("listing/<pk>/", views.TransportationDetailView.as_view(), name="transportation_detail"),
    path("listing-create/", views.TransportationCreateView.as_view(), name="transportation_create"),
    path("listing-update/<pk>/", views.TransportationUpdateView.as_view(), name="transportation_update"),
    path("listing-delete/<pk>/", views.TransportationDeleteView.as_view(), name="transportation_delete"),
]
