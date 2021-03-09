from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from django.views.generic.edit import FormView
from .forms import EventForm, ContactUsForm
from .models import Event, EventCategory, EventCity, EventState, FAQ, ContactUs
from cart.cart import Cart
from registration.forms import NewUserForm

# Create your views here.

class HomeView(TemplateView):
    """
    Only featured events are on the home page
    """
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        featured_events = Event.objects.filter(is_featured=True)
        first_item = featured_events.first()
        second_to_fourth_item = featured_events[1:4]
        context = super().get_context_data(**kwargs)
        context["featured_object"] = first_item
        context["featured_object_list"] = second_to_fourth_item
        return context


def search(request):
    """
    Search for events and filter search by city, state and category
    """
    queryset_list = Event.objects.order_by('-timestamp')

    # Keywords
    if 'query' in request.GET:
        query = request.GET['query']
        if query:
            queryset_list = queryset_list.filter(name__icontains=query)

    # get the id of the filter selected in search
    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            city_id = EventCity.objects.get(name__iexact=city).id
            queryset_list = queryset_list.filter(city=city_id)

    # State
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            state_id = EventState.objects.get(name__iexact=state).id
            queryset_list = queryset_list.filter(state=state_id)

    # Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            category_id = EventCategory.objects.get(name__iexact=category).id
            queryset_list = queryset_list.filter(category=category_id)

    template_name = 'core/search_list.html'
    context = {
        'query': request.GET['query'],
        'search_list': queryset_list,
        'categories' : EventCategory.objects.all(),
        'cities' : EventCity.objects.all(),
        'states' : EventState.objects.all(),
        }
    return render(request, template_name, context)


class EventListView(ListView):
    model = Event
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = EventCategory.objects.all()
        context['cities'] = EventCity.objects.all()
        context['states'] = EventState.objects.all()
        return context


class EventDetailView(DetailView):
    model = Event


class FAQListView(ListView):
    model = FAQ
    template_name = "core/help.html"


class EventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = EventForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context

    def form_valid (self, form):
        # if the form is valid, create and assign a value to the
        # user and slug fields in the EventForm modelform
        form.instance.creator = self.request.user
        form.instance.slug = slugify(form.instance.name)
        self.object = form.save()
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Event
    form_class = EventForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('registration:account')


class ContactUsView(CreateView):
    model = ContactUs
    form_class = ContactUsForm
    template_name = 'core/contact_us.html'
    success_url = reverse_lazy('registration:account')

    def form_valid(self, form):
        subject  = f"Contact from {form.instance.first_name} {form.instance.last_name}"
        message = form.instance.message
        sender = form.instance.email
        recipient_list = ['judeakinwale@gmail.com']
        # print(form.instance.email)
        send_mail(subject, message, sender, recipient_list)
        messages.success(self.request, "Contact inquiry sucessfully sent")
        return super().form_valid(form)


# class ContactView(FormView):
#     template_name = 'contact.html'
#     # form_class = ContactForm
#     success_url = '/thanks/'

#     def form_valid(self, form):
#         # This method is called when valid form data has been POSTed.
#         # It should return an HttpResponse.
#         form.send_email()
#         return super().form_valid(form)


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
    return render(request, 'cart/cart_detail.html')