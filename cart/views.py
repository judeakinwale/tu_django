from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Cart, CartItem
from core.models import Event

# Create your views here.

def view_cart(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        id = None

    if the_id is not None:
        total = 0.00
        for item in cart.cartitem_set.all():
            line_total = float(item.event.price) * item.quantity
            total += line_total

        request.session['items_total'] = cart.cartitem_set.count()
        cart.total = total
        cart.save()
        context = {'cart': cart}
    else:
        context = {
            'empty': True,
            'message': 'Your Cart is Empty'
        }
    template_name = 'cart/cart.html'
    return render(request, template_name, context)


def add_to_cart(request, slug):
    request.session.set_expiry(120000)
    try:
        the_id = request.session['cart_id']
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
    cart = Cart.objects.get(id=the_id)
    
    try:
        event = Event.objects.get(slug=slug)
    except:
        pass
    
    if request.method == 'POST':
        # quantity =  request.POST['qty']
        # for item in request.POST:
        #     key = item
        #     value = request.POST[key]
        cart_item = CartItem.objects.create(cart=cart, event=event)
        # cart_item.quantity = quantity
        cart_item.save()
    # NOTE: you can use redirect instead of httpresponseredirect. It even allows url names
    return HttpResponseRedirect('/cart')
    

def remove_from_cart(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        return HttpResponseRedirect('/cart')

    # try:
    #     cartitem = CartItem.objects.get(id=the_id)
    #     print(cart.cartitem_set.all())
    #     cartitem.cart = None
    #     cartitem = None
    #     cartitem.save()

    #     return HttpResponseRedirect('/cart')
    # except:
    #     return HttpResponseRedirect('/cart')