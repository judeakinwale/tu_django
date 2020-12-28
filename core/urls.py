from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'core'

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("forgot_password/", TemplateView.as_view(template_name='core/forgot_password.html'), name="forgot_password"),
    path("s/", views.search, name="search"),
    path("events/", views.EventListView.as_view(), name="event_list"),
    path("e/<slug>/", views.EventDetailView.as_view(), name="event_detail"),
    path("about/", TemplateView.as_view(template_name='core/about.html'), name="about"),
    path("faq/", views.faq, name="faq"),
    path("create-event/", TemplateView.as_view(template_name='core/create_event.html'), name="create_event"),
]
