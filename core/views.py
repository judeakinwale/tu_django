from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, View
from .models import Event

# Create your views here.

class HomeView(TemplateView):
    template_name = "core/index.html"

# class SearchListView(TemplateView):

#     def get(self, request):
#         template_name = "core/search_list.html"
#         query = self.request.Get.get('q')
#         try:
#             events = Event.objects.filter(name__icontains=query)
#             context = {"query": query, "search_result": events}
#         except:
#             context = {"query": query, "search_result": "invalid search query"}

#         return render(self.request, template_name, context)

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
