from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'registration'

urlpatterns = [
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("forgot_password/", TemplateView.as_view(template_name='registration/forgot_password.html'), name="forgot_password"),
    path("account/", TemplateView.as_view(template_name='registration/account.html'), name="account"),
]
