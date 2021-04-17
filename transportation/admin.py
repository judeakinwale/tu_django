from django.contrib import admin
from .models import Transportation, TransportationCategory

# Register your models here.

# @admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Vehicle details', {
            'fields': [
                'creator',
                'name',
                'description',
                'vehicle_type',
                'capacity',
            ]    
        }),
        ('Images', {
            'fields': [
                'photo_main',
                'photo_1',
                'photo_2',
                'photo_3',
                'photo_4',
            ]
        }),
        ('Location', {
            'fields': [
                'city',
                'state',
                'country'
                ]
        }),
    )

    list_display = [
        'name',
        'price',
        'vehicle_type',
        'capacity',
        'city',
        'state',
        'is_published',
        'is_booked',
        'is_featured',
    ]

    search_fields = [
        'name',
        'description',
        'vehicle_type'
        'city',
        'state',
    ]

    list_editable = ['is_published', 'is_featured']


admin.site.register(Transportation)
admin.site.register(TransportationCategory)
