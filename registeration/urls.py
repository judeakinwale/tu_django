from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'registeration'

urlpatterns = [
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("forgot_password/", TemplateView.as_view(template_name='core/forgot_password.html'), name="forgot_password"),
    path("account/", TemplateView.as_view(template_name='core/account.html'), name="account"),
]
