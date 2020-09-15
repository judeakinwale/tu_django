from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'core'

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("about/", TemplateView.as_view(template_name='core/about.html'), name="about"),
]
