from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'core'

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    # path("register/", views.register, name="register"),
    # path("logout/", views.logout_request, name="logout"),
    # path("login/", views.login_request, name="login"),
    # path("forgot_password/", TemplateView.as_view(template_name='core/forgot_password.html'), name="forgot_password"),
    # path("account/", TemplateView.as_view(template_name='core/account.html'), name="account"),
    path("s/", views.search, name="search"),
    path("events/", views.EventListView.as_view(), name="event_list"),
    path("e/<slug>/", views.EventDetailView.as_view(), name="event_detail"),
    path("about/", TemplateView.as_view(template_name='core/about.html'), name="about"),
    path("faq/", views.faq, name="faq"),
    path("create-event/", TemplateView.as_view(template_name='core/create_event.html'), name="create_event"),
    # path("payment-confirmation/", TemplateView.as_view(template_name='core/payment_confirmation.html'), name="payment_confirmation"),
    # path("cart/", views.cart, name="cart"),
    # path("cart/delete/", views.delete_cart, name="delete_cart"),
    # path("cart/add/<slug>/", views.add_to_cart, name="add_to_cart"),
    # path("cart/remove/<slug>/", views.remove_from_cart, name="remove_from_cart"),
    # path("checkout/", TemplateView.as_view(template_name='core/checkout.html'), name="checkout"),
    # path("contact/", TemplateView.as_view(template_name='core/contact_us.html'), name="contact_us"),
    
    # From django-shopping-cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]