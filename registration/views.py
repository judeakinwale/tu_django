from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View
from .forms import NewUserForm
from core.models import Event
from cart.cart import Cart
from payment.models import Payment

# Create your views here.

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
    return render(request, "registration/register.html", {"form": form})

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
    else:
        form = AuthenticationForm()
        # messages.error(request, "Unable to login")

    return render(request, "registration/login.html", {"form":form})


def user_account(request):
    user_events = Event.objects.filter(creator=request.user)
    template_name = "registration/account.html"
    context = {
        'object_list': user_events,
    }
    return render(request, template_name, context)

def delete_all_user_events(request):
    user_events = Event.objects.filter(creator=request.user)
    for event in user_events:
        event.delete()
    return redirect("registration:account")


def forgot_password(request):
    template_name = "registration/forgot_password.html"
    context = {}
    return render(request, template_name, context)