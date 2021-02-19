from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Listing, Realtor

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
