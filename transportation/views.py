from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import TransportationForm
from .models import Transportation, TransportationCategory
from core.models import EventCity, EventState
from core.search_filters import search_with_filters

# Create your views here.


search_filter_context = {
    'categories': TransportationCategory.objects.all(),
    'cities': EventCity.objects.all(),
    'states': EventState.objects.all(),
}


class SearchListView(ListView):
    model = Transportation
    paginate_by = 12
    template_name = "core/search_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'query' in self.request.GET:
            query = self.request.GET['query']
            queryset = Transportation.objects.order_by('-timestamp')
            queryset = queryset.filter(name__icontains=query)
            # print(queryset)
            queryset = search_with_filters(request=self.request, queryset=queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET['query']
        context["search_list"] = self.get_queryset()
        context.update(search_filter_context)
        return context


# def search(request):
#     queryset_list = Transportation.objects.order_by('-timestamp')

#     # Keywords
#     if 'query' in request.GET:
#         query = request.GET['query']
#         if query:
#             queryset_list = queryset_list.filter(name__icontains=query)

#     # City
#     if 'city' in request.GET:
#         city = request.GET['city']
#         if city:
#             city_id = EventCity.objects.get(name__iexact=city).id
#             queryset_list = queryset_list.filter(city=city_id)

#     # State
#     if 'state' in request.GET:
#         state = request.GET['state']
#         if state:
#             state_id = EventState.objects.get(name__iexact=state).id
#             queryset_list = queryset_list.filter(state=state_id)

#     # Category
#     if 'category' in request.GET:
#         category = request.GET['category']
#         if category:
#             category_id = TransportationCategory.objects.get(name__iexact=category).id
#             queryset_list = queryset_list.filter(category=category_id)

#     template_name = 'core/search_list.html'
#     context = {
#         'query': request.GET['query'],
#         'search_list': queryset_list,
#         'categories': TransportationCategory.objects.all(),
#         'cities': EventCity.objects.all(),
#         'states': EventState.objects.all(),
#     }
#     return render(request, template_name, context)


class TransportationListView(ListView):
    model = Transportation
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = TransportationCategory.objects.all()
        context['cities'] = EventCity.objects.all()
        context['states'] = EventState.objects.all()
        return context


class TransportationDetailView(DetailView):
    model = Transportation


class TransportationCreateView(LoginRequiredMixin, CreateView):
    model = Transportation
    form_class = TransportationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class TransportationUpdateView(LoginRequiredMixin, UpdateView):
    model = Transportation
    form_class = TransportationForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context


class TransportationDeleteView(LoginRequiredMixin, DeleteView):
    model = Transportation
    # template_name = "transportation/transportation_confirm_delete.html"
    success_url = reverse_lazy('registration:account')
