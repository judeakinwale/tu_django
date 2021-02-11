from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Event
from cart.cart import Cart
from registration.forms import NewUserForm

# Create your views here.

class HomeView(TemplateView):
    template_name = "core/index.html"


def search(request):
    template_name = 'core/search_list.html'
    try:
        query = request.GET.get('q')
        events = Event.objects.filter(name__icontains=query)
        context = {'query': query, 'search_result': events}
    except:
        context = {'query': query, 'search_list': 'Sorry, that event does not exist or has take place'}
    return render(request, template_name, context)

def faq(request):
    return render(request, "core/help.html")

class EventListView(ListView):
    model = Event
    paginate_by = 9
    template_name = "core/event_list.html"

class EventDetailView(DetailView):
    model = Event
    template_name = "core/event_detail.html"

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


@login_required(login_url="/users/login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')