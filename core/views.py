from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Event, FAQ
from .forms import EventForm
from cart.cart import Cart
from registration.forms import NewUserForm

# Create your views here.

# class HomeView(ListView):
#     model = Event
#     template_name = "core/index.html"

def home(request):
    featured_events = Event.objects.filter(featured=True)
    first_featured = featured_events.first()
    other_featured = featured_events[1:4]
    template_name = "core/index.html"
    context = {"featured_object_list": other_featured, 'featured_object': first_featured}
    return render(request, template_name, context)


def search(request):
    template_name = 'core/search_list.html'
    try:
        query = request.GET.get('q')
        events = Event.objects.filter(name__icontains=query)
        context = {'query': query, 'search_result': events}
    except:
        context = {'query': query, 'search_list': 'Sorry, that event does not exist or has take place'}
    return render(request, template_name, context)


class EventListView(ListView):
    model = Event
    paginate_by = 9
    template_name = "core/event_list.html"

class EventDetailView(DetailView):
    model = Event
    template_name = "core/event_detail.html"


class FAQListView(ListView):
    model = FAQ
    template_name = "core/help.html"


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = EventForm()
    template_name = "core/create_event.html"
    context = {'form': form}
    return render(request, template_name, context)

# From django-shopping-cart
@login_required(login_url="/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Event.objects.get(id=id)
    cart.add(product=product)
    return redirect("core:event_list")


@login_required(login_url="/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Event.objects.get(id=id)
    cart.remove(product)
    return redirect("core:cart_detail")


@login_required(login_url="/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Event.objects.get(id=id)
    cart.add(product=product)
    return redirect("core:cart_detail")


@login_required(login_url="/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Event.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("core:cart_detail")


@login_required(login_url="/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("core:cart_detail")


@login_required(login_url="/login")
def cart_detail(request):
    total = 0
    print(request.session['cart'])
    # # if request.session.cart.items:
    for item in request.session['cart']:
        print(item)
    #     print(value)
        # print(int(value['price']))
        # total += int(value['price']) * int(value['quantity'])

    return render(request, 'cart/cart_detail.html', {'total': total})