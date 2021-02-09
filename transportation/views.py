from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Transportation, TransportationCategory

# Create your views here.

def search(request):
    template_name = 'core/search_list.html'
    try:
        query = request.GET.get('q')
        events = Event.objects.filter(name__icontains=query)
        context = {'query': query, 'search_result': events}
    except:
        context = {'query': query, 'search_list': 'Sorry, that event does not exist or has take place'}
    return render(request, template_name, context)


class TransportationListView(ListView):
    model = Transportation
    paginate_by = 9
    template_name = "transportation/transportation_list.html"


class TransportationDetailView(DetailView):
    model = Transportation
    template_name = "transportation/transportation_detail.html"
