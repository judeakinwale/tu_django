from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Listing, Realtor

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


class ListingListView(ListView):
    model = Listing
    paginate_by = 9
    template_name = "location/location_list.html"


class ListingDetailView(DetailView):
    model = Listing
    template_name = "location/location_detail.html"
