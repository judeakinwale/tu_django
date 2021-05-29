from django.urls import path
# from django.views.generic import TemplateView
from . import views


app_name = 'registration'

urlpatterns = [
    path("register/", views.register, name="register"),
    path("logout/", views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),
    path("account/", views.user_account, name="account"),
    path("delete-all-user-events/", views.delete_all_user_events, name="delete_all_user_events")
]
