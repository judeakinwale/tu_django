from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Cart, CartItem
from core.models import Event

# Create your views here.
def cartId(request):
  session_cart_id = request.session['cart_id']
  return session_cart_id

def view_cart(request):
  # user = request.user
  # Check if a cart is associated with the user
  #   If associated, view cart and it's contents
  try:
    if request.user.is_authenticated:
      cart = Cart.objects.filter(user=request.user, ordered=False).first()
    # else:
    #   cart = Cart.objects.filter(id=cartId(request), ordered=False).first()
    template_name = 'cart/cart.html'
    context = {'object_list': cart.items.all(), 'total': cart.get_total()}
    return render(request, template_name, context)
  #   Else, error message  
  except:
    messages.error(request, "You do not have an active order")
    return redirect("core:event_list")

def add_to_cart(request, slug):
  # Define variables needed for the view
  item = get_object_or_404(Event, slug=slug)
  cart_item, created = CartItem.objects.get_or_create(item=item, ordered=False)
  # Check if user is logged in
  if Cart.objects.filter(user=request.user, ordered=False).first() or cart.objects.filter(id=cartId(), ordered=False).first():
    cart_qs = Cart.objects.filter(user=request.user, ordered=False).first() or cart.objects.filter(id=cartId(), ordered=False).first()
    try:
      cartitem_qs = cart_qs.items.filter(item__slug=slug)
      cartitem_qs += 1
      cartitem_qs.save()
      messages.info(request, "Ticket quantity has been updated")
      return redirect("cart:view_cart")
    except:
      cart_qs.items.add(cart_item)
      messages.info(request, "This event was added to your cart")
      return redirect("cart:view_cart")
  else:
    request.session.set_expiry(120000)
    new_cart = Cart.objects.create()
    new_cart.items.add(cart_item)
    new_cart.save()
    request.session['cart_id'] = new_cart.id

    messages.info(request, "This event was added to your cart")
    return redirect("core:cart")
  #   If user is not logged in create a session and cart id for the user
  # Find cart associated with user
  #   If no cart is associated with the user create a new cart, linking it to the user
  #   If cart is associated with the user, check if selected event is in the cart
  #     If selected event is in the cart increase the quantity
  #     If selected event is not in the cart add selected event to cart
  # pass

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