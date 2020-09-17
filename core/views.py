from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Event

# Create your views here.

class HomeView(TemplateView):
    template_name = "core/index.html"

class EventListView(ListView):
    model = Event
    template_name = "core/event_list.html"

class EventDetailView(DetailView):
    model = Event
    template_name = "core/event_detail.html"
