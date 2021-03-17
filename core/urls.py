from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = 'core'

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("s/", views.search, name="search"),
    path("events/", views.EventListView.as_view(), name="event_list"),
    path("event/<slug>/", views.EventDetailView.as_view(), name="event_detail"),
    path("faq/", views.FAQListView.as_view(), name="faq"),
    path("create/", views.EventCreateView.as_view(), name="create_event"),
    path("update/<slug>/", views.EventUpdateView.as_view(), name="update_event"),
    path("delete/<slug>/", views.EventDeleteView.as_view(), name="delete_event"),
    path('contact-us/', views.ContactUsView.as_view(), name='contact_us'),

    # From django-shopping-cart
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
]

handler404 = 'core.views.my_custom_page_not_found_view'