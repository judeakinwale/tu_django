from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils import timezone
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, TemplateView, CreateView, DeleteView, UpdateView
from .forms import EventForm
from .models import Event, EventCategory, EventCity, EventState, FAQ
# from .forms import EventForm
from cart.cart import Cart
from registration.forms import NewUserForm

# Create your views here.

# class HomeView(ListView):
#     model = Event
#     template_name = "core/index.html"

# def home(request):
#     featured_events = Event.objects.filter(featured=True)
#     first_featured = featured_events.first()
#     other_featured = featured_events[1:4]
#     template_name = "core/index.html"
#     context = {"featured_object_list": other_featured, 'featured_object': first_featured}
#     return render(request, template_name, context)


class HomeView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        featured_events = Event.objects.filter(featured=True)
        first_item = featured_events.first()
        second_to_fourth_item = featured_events[1:4]
        context = super().get_context_data(**kwargs)
        context["featured_object"] = first_item
        context["featured_object_list"] = second_to_fourth_item
        return context




def search(request):
    queryset_list = Event.objects.order_by('-timestamp')

    # Keywords
    if 'query' in request.GET:
        query = request.GET['query']
        if query:
            queryset_list = queryset_list.filter(name__icontains=query)

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
            # print (EventState.objects.get(name__iexact=state))
            state_id = EventState.objects.get(name__iexact=state).id
            # print (EventState.objects.filter(name__iexact=state))
            queryset_list = queryset_list.filter(state=state_id)

    # Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            category_id = EventCategory.objects.get(name__iexact=category).id
            queryset_list = queryset_list.filter(category=category_id)


    # try:
    #     query = request.GET.get('q')
    #     events = Event.objects.filter(name__icontains=query)
    #     context = {'query': query, 'search_result': events}
    # except:
    template_name = 'core/search_list.html'
    context = { 'query': request.GET['query'], 
                'search_list': queryset_list,
                'categories' : EventCategory.objects.all(),
                'cities' : EventCity.objects.all(),
                'states' : EventState.objects.all(),
                }
    return render(request, template_name, context)


class EventListView(ListView):
    model = Event
    paginate_by = 9
    # template_name = "core/event_list.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = EventCategory.objects.all()
        context['cities'] = EventCity.objects.all()
        context['states'] = EventState.objects.all()
        return context
    


class EventDetailView(DetailView):
    model = Event
    # print(Event.objects.get(id=1).start_time)
    # template_name = "core/event_detail.html"


class FAQListView(ListView):
    model = FAQ
    template_name = "core/help.html"


class EventCreateView(CreateView):
    model = Event
    form_class = EventForm
    # fields = ['name', 'description', 'category', 'image', 'price', 'sale_price', 'slug'] 
    # fields = '__all__'
    # template_name = "core/event_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context

    def form_valid (self, form):
        form.instance.user = self.request.user
        form.instance.slug = slugify(form.instance.name)
        self.object = form.save()
        return super().form_valid(form)

@login_required(login_url="/login")
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        print (form)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.slug = slugify(post.name)
            # handle_uploaded_file(request.Files['image'])
            post.save()
            return redirect('core:event_list')
    else:
        form = EventForm()

    template_name = 'core/event_form.html'
    context = {
        'title': 'Create',
        'form': form,
    }
    return render(request, template_name, context)

class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    # fields = '__all__'
    # template_name = "TEMPLATE_NAME"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context
    


class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('registration:account')
    # template_name = "core/event_confirm_delete.html"


def contact_us(request):
    template_name = 'core/contact_us.html'
    return render(request, template_name)

# def create_event(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect("core:homepage")
#     else:
#         form = EventForm()
#         template_name = "core/create_event.html"
#         context = {'form': form}
#         return render(request, template_name, context)

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