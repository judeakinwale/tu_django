from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
from .forms import ListingForm
from .models import Listing, ListingCategory
from core.models import EventCity, EventState
from core.search_filters import search_with_filters

# Create your views here.


search_filter_context = {
    'categories': ListingCategory.objects.all(),
    'cities': EventCity.objects.all(),
    'states': EventState.objects.all(),
}


class SearchListView(ListView):
    model = Listing
    paginate_by = 12
    template_name = "core/search_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'query' in self.request.GET:
            query = self.request.GET['query']
            queryset = Listing.objects.order_by('-timestamp')
            queryset = queryset.filter(title__icontains=query)
            queryset = search_with_filters(request=self.request, queryset=queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["query"] = self.request.GET['query']
        context["search_list"] = self.get_queryset()
        context.update(search_filter_context)
        return context


# def search(request):
#     # Keywords
#     if 'query' in request.GET:
#         query = request.GET['query']
#         queryset = Listing.objects.order_by('-timestamp')
#         queryset = search_with_filters(query=query, request=request, queryset=queryset)

#     template_name = 'core/search_list.html'
#     context = {
#         'query': request.GET['query'],
#         'object_list': queryset,
#         'search_list': queryset,
#     }
#     context.update(search_filter_context)
#     return render(request, template_name, context)


class ListingListView(ListView):
    model = Listing
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(search_filter_context)
        return context


class ListingDetailView(DetailView):
    model = Listing


class ListingCreateView(LoginRequiredMixin, CreateView):
    model = Listing
    form_class = ListingForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
        form.instance.creator = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class ListingUpdateView(LoginRequiredMixin, UpdateView):
    model = Listing
    form_class = ListingForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context


class ListingDeleteView(LoginRequiredMixin, DeleteView):
    model = Listing
    success_url = reverse_lazy('registration:account')
