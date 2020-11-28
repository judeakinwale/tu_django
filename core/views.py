from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView, View
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .models import Event
from .forms import NewUserForm

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


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            messages.info(request, f"You are logged in as {username}")
            return redirect("core:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = NewUserForm
    return render(request, "core/register.html", {"form": form})

def logout_request(request):
    logout(request)
    messages.info(request, "You've logged out")
    return redirect("core:homepage")


def login_request(request):
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.info(request, f"You are logged in as {username}")
                return redirect("core:homepage")
            else:
                messages.error(request, "Invalid Username or Password")
        else:
            messages.error(request, "Invalid Username or Password")
    
    form = AuthenticationForm()
    return render(request, "core/login.html", {"form":form})