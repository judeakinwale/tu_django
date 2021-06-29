from .models import EventCity, EventState, EventCategory
from location.models import ListingCategory
from transportation.models import TransportationCategory


def search_with_filters(request, queryset):
    """Search through a queryset using filters"""
    queryset = location_filter(request=request, queryset=queryset)
    queryset = category_filter(request=request, queryset=queryset)
    return queryset


def location_filter(request, queryset):
    """Filter search query by location - city and state"""

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            # Get the id of the city selected in search
            city_id = EventCity.objects.get(name__iexact=city).id
            queryset = queryset.filter(city=city_id)
            print(request.path)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            # Get the id of the state selected in search
            state_id = EventState.objects.get(name__iexact=state).id
            queryset = queryset.filter(state=state_id)

    return queryset


def category_filter(request, queryset):
    """Filter search by category, depending on the app"""

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            # Confirm the current app and Get the id of the category selected in search
            if '/l/' in request.path:  # For location (venue)
                category_id = ListingCategory.objects.get(name__iexact=category).id
                print('/l/')
            elif '/t/' in request.path:  # For transportation
                category_id = TransportationCategory.objects.get(name__iexact=category).id
            else:  # For events
                category_id = EventCategory.objects.get(name__iexact=category).id

            queryset = queryset.filter(category=category_id)

    return queryset
