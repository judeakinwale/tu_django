from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View, FormView
from .forms import CustomerInfoForm
from .models import Payment, BillingAddress, Order, UserOrder, PaymentConfirmation
from core.models import Event
from location.models import Listing
from transportation.models import Transportation
from cart.context_processor import cart_total_amount
from cart.cart import Cart
from paystack.api.signals import payment_verified, event_signal
from django.dispatch import receiver


# Create your views here.

def customer_info(request):
    if request.method == "POST":
        customer_form = CustomerInfoForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return render(request, 'payment/payment.html', {'email':"human@jjj.co"})
        else:
            return HttpResponse('Invalid input try again!!!')
    else:
        customer_form = CustomerInfoForm()
    return render(request, 'payment/customer_info.html', {'customer_form': customer_form})


def checkout(request):
    order_qs = Order.objects.filter(user=request.user, is_ordered=False)
    # for key, value in request.session['cart'].items():
    #     if Event.objects.filter(slug=value.slug):
    #         event = Event.objects.filter(slug=value.slug)
    #         date_time_value = event.slug
    total_amount = cart_total_amount(request)["cart_total_amount"]
    # print(total_amount)
    template_name = "payment/checkout.html"
    context = {'total': total_amount, 'email': request.user.email}
    return render(request, template_name, context)


@login_required(login_url="/login")
def direct_checkout(request, target, id):

    if target == 'location':
        query = Listing.objects.get(id=id)

    elif target == 'transport':
        query = Transportation.objects.get(id=id)

    elif target == 'event':
        query = Event.objects.get(id=id)

    else:
        messages.error(request, "Invalid option for direct checkout")

    # if request.session['cart']:
    #     # print(query.price)
    #     # print (request.session['cart'].keys()[0])
    #     cart_dict = request.session['cart']
    #     # print (cart_dict[cart_dict.keys()[0]])
    #     # cart_keys = cart_dict.keys()
    #     cart_key = next(iter(cart_dict))
    #     print(cart_dict[cart_key])
    #     # for key, value in request.session['cart'].items().first():
    #     # print (key)

    if not UserOrder.objects.filter(user=request.user, is_ordered=False):
        Cart(request).clear()

    Cart(request).add(query)

    if request.session['cart']:
        cart_dict = request.session['cart']
        cart_keys = cart_dict.keys()
        cart_key = next(iter(cart_dict))
        cart_query = cart_dict[cart_key]
        print(cart_query)
        cart_arr = []
        cart_item_qty = []
        cart_events = []

        if UserOrder.objects.filter(user=request.user):
            user_order = UserOrder.objects.filter(user=request.user).first()

        else:
            # Cart(request).clear()
            user_order = UserOrder()

            user_order.user = request.user

        for key in cart_keys:
            cart_arr.append(key)
            cart_events.append(Event.objects.get(id=key))
            # user_order.order_items.set(Event.objects.filter(id=key))
            cart_item_qty.append(cart_dict[key]['quantity'])
            print(key)

        print(cart_arr)


        # user_order.order_items.set(query)
        user_order.cart_id = cart_arr
        user_order.order_item_qty = cart_item_qty
        user_order.amount_due = cart_total_amount(request)["cart_total_amount"]
        user_order.save()
        user_order.order_items.clear()
        for key in cart_keys:
            user_order.order_items.add(Event.objects.get(id=key))
        user_order.save()



    template_name = "payment/direct_checkout.html"
    context = {
        'object': query,
        'total': query.price,
    }
    return render(request, template_name, context)

# Paystack Signals
@receiver(payment_verified)
def on_payment_verified(sender, ref,amount, **kwargs):
    """
    ref: paystack reference sent back.
    amount: amount in Naira.
    """
    confirmation = PaymentConfirmation()
    confirmation.user = request.user
    confirmation.amount = cart_total_amount(request)["cart_total_amount"]
    pass


@receiver(event_signal)
def on_event_received(sender, event, data, **kwargs):
    # sender is the raw request
    # event is the event name that was passed https://developers.paystack.co/docs/events
    # data is the available data tied to the event
    pass
