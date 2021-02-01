from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Cart

# Create your views here.
def cartId(request):
  session_cart_id = request.session['cart_id']
  return session_cart_id

def view_cart(request):
  # Check if a cart is associated with the user
  #   If associated, view cart and it's contents
  if Cart.objects.filter(user=request.user, ordered=False).first() or cart.objects.filter(id=cartId(), ordered=False).first():
    template_name = 'cart/cart.html'
    context = {'object_list': Cart.items.all(), 'total': Cart.get_total()}
    return render(request, template_name, context)
  #   Else, error message  
  else:
    messages.error(request, "You do not have an active order")
    return redirect("core:event_list")

def add_to_cart(request):
  # Check if user is logged in
  #   If user is not logged in create a session and cart id for the user
  # Find cart associated with user
  #   If no cart is associated with the user create a new cart, linking it to the user
  #   If cart is associated with the user, check if selected event is in the cart
  #     If selected event is in the cart increase the quantity
  #     If selected event is not in the cart add selected event to cart
  pass

def remove_from_cart(request):
  # Check if a cart is associated with the user
  #   If associated, check if selected cart item is in cart
  #     If in cart, check if quantity is greater than 1
  #       If greater than 1, reduce quantity
  #       Else, delete item
  #     If not not in cart, send error message
  #   If not associated, send error message
  pass

def delete_cart(request):
  # Check if a cart is associated with the user
  #   If associated, delete cart
  #   If not associated, send error message
  pass