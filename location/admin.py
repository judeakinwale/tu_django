from django.contrib import admin
from .models import Listing, ListingCategory

# Register your models here.


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Listing Details', {
            'fields': [
                'creator',
                'title',
                'description',
                'price',
                'category',
            ]
        }),
        ('Address', {
            'fields': [
                'street_address',
                'city',
                'state',
                'zipcode',
                'country',
            ]
        }),
        ('Extra Details', {
            'fields': [
                'bedrooms',
                'bathrooms',
                'pools',
                'lot_size',
            ]
        }),
        ('Images', {
            'fields': [
                'photo_main',
                'photo_1',
                'photo_2',
                'photo_3',
                'photo_4',
                'photo_5',
                'photo_6',
            ]
        }),
        ('Filters', {
            'fields': ['is_published', 'is_booked', 'is_featured']
        }),
    )

    list_display = [
        'title',
        'price',
        'category',
        'street_address',
        'city',
        'state',
        'is_published',
        'is_booked',
        'is_featured',
    ]

    search_fields = [
        'title',
        'description',
        'category'
        'street_address'
        'city',
        'state',
    ]

    list_editable = ['is_published', 'is_featured', 'is_booked']


admin.site.register(ListingCategory)
