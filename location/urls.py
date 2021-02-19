from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'location'

urlpatterns = [
    path("listings/", views.ListingListView.as_view(), name="location_list"),
    path("listing/<pk>/", views.ListingDetailView.as_view(), name="location_detail"),
    path("listing/create/", views.ListingCreateView.as_view(), name="location_create"),
    path("listing/update/<pk>/", views.ListingUpdateView.as_view(), name="location_update"),
    path("listing/delete/<pk>/", views.ListingDeleteView.as_view(), name="location_delete"),
]
