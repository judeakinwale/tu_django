from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'location'

urlpatterns = [
    path("", views.ListingListView.as_view(), name="location_list"),
    path("create/", views.ListingCreateView.as_view(), name="location_create"),
    path("<pk>/", views.ListingDetailView.as_view(), name="location_detail"),
    path("<pk>/update/", views.ListingUpdateView.as_view(), name="location_update"),
    path("<pk>/delete/", views.ListingDeleteView.as_view(), name="location_delete"),
]
