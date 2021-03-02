from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Listing, Realtor, ListingCategory
from core.models import EventCity, EventState

# Create your views here.

def search(request):
    template_name = 'core/search_list.html'
    try:
        query = request.GET.get('q')
        listing = Listing.objects.filter(name__icontains=query)
        context = {'query': query, 'search_result': listing}
    except:
        context = {'query': query, 'search_list': 'Sorry, that event does not exist or has take place'}
    return render(request, template_name, context)


def search(request):
    queryset_list = Listing.objects.order_by('-timestamp')

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
            state_id = EventState.objects.get(name__iexact=state).id
            queryset_list = queryset_list.filter(state=state_id)

    # Category
    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            category_id = ListingCategory.objects.get(name__iexact=category).id
            queryset_list = queryset_list.filter(category=category_id)

    template_name = 'core/search_list.html'
    context = {
        'query': request.GET['query'],
        'search_list': queryset_list,
        'categories': EventCategory.objects.all(),
        'cities': EventCity.objects.all(),
        'states': EventState.objects.all(),
    }
    return render(request, template_name, context)


class ListingListView(ListView):
    model = Listing
    paginate_by = 9
    template_name = "location/listing_list.html"


class ListingDetailView(DetailView):
    model = Listing
    template_name = "location/listing_detail.html"



class ListingCreateView(CreateView):
    model = Listing
    fields = '__all__'
    template_name = "location/listing_form.html"



class ListingUpdateView(UpdateView):
    model = Listing
    fields = '__all__'
    template_name = "location/listing_form.html"

class ListingDeleteView(DeleteView):
    model = Listing
    template_name = "location/listing_confirm_delete.html"
