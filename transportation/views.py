from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Transportation, TransportationCategory
from core.models import EventCity, EventState


# Create your views here.

# def search(request):
#     template_name = 'core/search_list.html'
#     try:
#         query = request.GET.get('q')
#         transport = Transportation.objects.filter(name__icontains=query)
#         context = {'query': query, 'search_result': transport}
#     except:
#         context = {'query': query, 'search_list': 'Sorry, that event does not exist or has take place'}
#     return render(request, template_name, context)


def search(request):
    queryset_list = Transportation.objects.order_by('-timestamp')

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
            category_id = TransportationCategory.objects.get(name__iexact=category).id
            queryset_list = queryset_list.filter(category=category_id)

    template_name = 'core/search_list.html'
    context = {
        'query': request.GET['query'],
        'search_list': queryset_list,
        'categories': TransportationCategory.objects.all(),
        'cities': EventCity.objects.all(),
        'states': EventState.objects.all(),
    }
    return render(request, template_name, context)


class TransportationListView(ListView):
    model = Transportation
    paginate_by = 9
    # template_name = "transportation/listingtransportation_list.html"


class TransportationDetailView(DetailView):
    model = Transportation
    # template_name = "transportation/transportation_detail.html"


class TransportationCreateView(LoginRequiredMixin, CreateView):
    model = Transportation
    fields = '__all__'
    # template_name = "transportation/transportation_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     form.instance.slug = slugify(form.instance.name)
    #     self.object = form.save()
    #     return super().form_valid(form)


class TransportationUpdateView(LoginRequiredMixin, UpdateView):
    model = Transportation
    fields = '__all__'
    # template_name = "transportation/transportation_form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context


class TransportationDeleteView(LoginRequiredMixin, DeleteView):
    model = Transportation
    template_name = "transportation/transportation_confirm_delete.html"