from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags
# from django.views.generic import ListView, DetailView, TemplateView, View, FormView
from .forms import CustomerInfoForm
from .models import UserOrder, PaymentConfirmation  # , Payment, BillingAddress, Order
from core.models import Event
from location.models import Listing
from transportation.models import Transportation
# From django-shopping-cart
from cart.cart import Cart
from cart.context_processor import cart_total_amount
# For pypaystack
from django.dispatch import receiver
from paystack.api.signals import payment_verified, event_signal
from datetime import date, datetime, timedelta
import pytz

# Create your views here.


def customer_info(request):
    if request.method == "POST":
        customer_form = CustomerInfoForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return render(request, 'payment/payment.html', {'email': "human@jjj.co"})
        else:
            return HttpResponse('Invalid input try again!!!')
    else:
        customer_form = CustomerInfoForm()
    return render(request, 'payment/customer_info.html', {'customer_form': customer_form})


@login_required(login_url="/login")
def checkout(request):
    context = {}
    if UserOrder.objects.filter(user=request.user, is_ordered=False):
        user_order = UserOrder.objects.filter(user=request.user, is_ordered=False).first()
    else:
        user_order = UserOrder()
        user_order.user = request.user

    if request.session['cart']:
        cart_dict = request.session['cart']
        cart_keys = cart_dict.keys()

        # Get the first key in session['cart']
        # cart_key = next(iter(cart_dict))

        # Get the value of the first key
        # cart_query = cart_dict[cart_key]

        # TODO: Use cart query

        cart_arr = []
        cart_item_qty = []
        cart_events = []

        for key in cart_keys:
            cart_arr.append(key)
            cart_events.append(Event.objects.get(id=key))
            cart_item_qty.append(cart_dict[key]['quantity'])

        # Store cart_arr and cart_item_qty in UserOrder
        user_order.cart_id = cart_arr
        user_order.order_item_qty = cart_item_qty
        user_order.amount_due = cart_total_amount(request)["cart_total_amount"]
        user_order.save()
        user_order.order_items.clear()
        for key in cart_keys:
            user_order.order_items.add(Event.objects.get(id=key))
        user_order.save()

        if request.method == "GET":

            # user_order.ticket_name = request.GET['user_name']
            full_name = f"{request.user.first_name} {request.user.last_name}"
            user_order.ticket_name = request.GET.get('user_name', full_name)

            # user_order.ticket_email = request.GET['user_email']
            email_address = request.user.email
            user_order.ticket_email = request.GET.get('user_email', email_address)

            user_order.save()
            context_2 = {'user_order': user_order}
            context.update(context_2)

    total_amount = cart_total_amount(request)["cart_total_amount"]
    template_name = "payment/checkout.html"
    context_3 = {'total': total_amount, 'email': request.user.email}
    context.update(context_3)
    return render(request, template_name, context)


@login_required(login_url="/login")
def direct_checkout(request, target, id):
    context = {}
    # Confirm which app the checkout is coming from
    if target == 'location':
        query = Listing.objects.get(id=id)

    elif target == 'transport':
        query = Transportation.objects.get(id=id)

    elif target == 'event':
        query = Event.objects.get(id=id)

    else:
        messages.error(request, "Invalid option for direct checkout")

    # Clear previous Cart if user is not set and ordered is false
    if not UserOrder.objects.filter(user=request.user, is_ordered=False):
        Cart(request).clear()

    if UserOrder.objects.filter(user=request.user, is_ordered=True):
        Cart(request).clear()

    Cart(request).add(query)

    if request.session['cart']:
        cart_dict = request.session['cart']
        cart_keys = cart_dict.keys()

        # Get the first key in session['cart']
        # cart_key = next(iter(cart_dict))

        # Get the value of the first key
        # cart_query = cart_dict[cart_key]

        # TODO: Use cart query

        cart_arr = []
        cart_item_qty = []
        cart_events = []

        # Update UserOrder or Create new UserOrder if one doesn't exist
        if UserOrder.objects.filter(user=request.user, is_ordered=False):
            user_order = UserOrder.objects.filter(user=request.user, is_ordered=False).first()

        else:
            user_order = UserOrder()
            user_order.user = request.user

        for key in cart_keys:
            cart_arr.append(key)
            cart_events.append(Event.objects.get(id=key))
            # user_order.order_items.add(Event.objects.get(id=key))
            cart_item_qty.append(cart_dict[key]['quantity'])

        # Store cart_arr and cart_item_qty in UserOrder
        user_order.cart_id = cart_arr
        user_order.order_item_qty = cart_item_qty
        user_order.amount_due = cart_total_amount(request)["cart_total_amount"]
        user_order.save()
        user_order.order_items.clear()
        for key in cart_keys:
            user_order.order_items.add(Event.objects.get(id=key))
        user_order.save()

        if request.method == "GET":

            # user_order.ticket_name = request.GET['user_name']
            full_name = f"{request.user.first_name} {request.user.last_name}"
            user_order.ticket_name = request.GET.get('user_name', full_name)

            # user_order.ticket_email = request.GET['user_email']
            email_address = request.user.email
            user_order.ticket_email = request.GET.get('user_email', email_address)

            user_order.save()
            context_2 = {'user_order': user_order}
            context.update(context_2)

        return redirect("payment:checkout")

    total_amount = cart_total_amount(request)["cart_total_amount"]
    template_name = "payment/direct_checkout.html"
    context_3 = {'object': query, 'total': total_amount}
    context.update(context_3)
    return render(request, template_name, context)


# Paystack Signals
@receiver(payment_verified)
def on_payment_verified(sender, ref, amount, *args, **kwargs):
    """
    ref: paystack reference sent back.
    amount: amount in Naira.
    """
    confirmation = PaymentConfirmation()
    confirmation.sender = sender
    confirmation.raw_request = sender
    # confirmation.user_order = UserOrder.objects.filter(user=request.user, is_ordered=False).first()
    confirmation.reference = ref
    confirmation.amount = amount
    confirmation.save()


@receiver(event_signal)
def on_event_received(sender, event, data, **kwargs):
    """
    sender: the raw request
    event: the event name that was passed https://developers.paystack.co/docs/events
    data: the available data tied to the event
    """
    confirmation = PaymentConfirmation(raw_request=sender)
    confirmation.event = event
    confirmation.data = data
    confirmation.save()

    return redirect("payment:payment_confirmation")


def payment_confirmation(request):
    """
    confirm payment and send tickets by mail
    """
    user_order = UserOrder.objects.filter(user=request.user, is_ordered=False).first()
    print(user_order)
    if user_order:
        user_order.is_ordered = True
        Cart(request).clear()
        order_items = user_order.order_items.all()
        if request.method == "GET":
            user_order.ticket_name = request.GET['user_name']
            user_order.ticket_email = request.GET['user_email']
        user_order.save()

        subject = 'Ticket Testing'
        html_message = render_to_string(
            'mail/ticket.html',
            {
                'context': 'Templating and context works',
                'order_items': order_items,
                'user': request.user.username,
                'user_order': user_order,
            })
        plain_message = strip_tags(html_message)
        from_email = 'From <judeakinwale@gmail.com>'
        to = [f'{user_order.ticket_email}']
        send_mail(
            subject,
            plain_message,
            from_email,
            to,
            html_message=html_message,
            fail_silently=True,
        )

        messages.success(request, 'A ticket has been sent to your mail')

        # total_amount = cart_total_amount(request)["cart_total_amount"]
        # if total_amount != 0.00:
        #     return redirect("payment:payment_confirmation")

        template_name = 'paystack/success-page.html'

    else:
        messages.error(request, 'There was an error in your order')

        template_name = 'paystack/failed-page.html'

    context = {

    }
    return render(request, template_name, context)


# def event_creator_attendee_list_email(request):
def event_creator_attendee_list_email():
    today = datetime.now(tz=timezone.utc)
    # week_before = (date.today()-timedelta(days=7)).isoformat()
    # week_after = (date.today()+timedelta(days=7)).isoformat()
    week_after = (today+timedelta(days=7)).isoformat()
    events = Event.objects.filter(start_time__contains=week_after)

    if events.exists():
        for item in events:
            creator = item.creator
            user_order = UserOrder.objects.filter(is_ordered=True, order_items=item)
            # for order_item in user_order:
            #     print(creator.email)
            #     print(order_item)
            #     print(order_item.user)
            #     print(order_item.ticket_id)
            #     print(order_item.ticket_name)
            #     print(order_item.ticket_email)
            subject = 'Attendee List'
            html_message = render_to_string(
                'mail/attendee_list_email.html',
                {
                    # 'context': 'Templating and context works',
                    # 'order_items': order_items,
                    # 'user': request.user.username,
                    'user': creator,
                    'object_list': user_order,
                })
            plain_message = strip_tags(html_message)
            from_email = 'From <judeakinwale@gmail.com>'
            to = [f'{creator.email}']
            send_mail(
                subject,
                plain_message,
                from_email,
                to,
                html_message=html_message,
                fail_silently=True,
            )

        # messages.success(request, 'Attendee list has been sent to your mail')

    else:
        # messages.error(request, 'There are no applicable events')
        pass
    # print(events)
    # template_name = 'mail/attendee_list_email.html'
    # context = {}
    # return redirect('registration:account')
    # return redirect(request.META['HTTP_REFERER'])
    # return render(request, template_name, context)


def delete_outdated_events():
    today = datetime.now(tz=timezone.utc)
    # tomorrow = (date.today()+timedelta(days=1)).isoformat()
    tomorrow = (today+timedelta(days=1)).isoformat()
    events = Event.objects.filter(start_time__lte=tomorrow)
    # print(events)
    if events.exists():
        for item in events:
            print(item)
            # item.delete()
