from django.contrib import admin
from .models import Event, EventCategory, EventCity, EventState, FAQ, ContactUs, Profile

# Register your models here.


# @admin.register()
class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Event Details', {
            'fields': [
                'creator',
                'name',
                'description',
                'image',
                ]
        }),
        ('Category', {
            'fields': ['category']
        }),
        ('Tickets', {
            'fields': [
                'ticket_price',
                'ticket_sale_price',
                'ticket_quantity',
                'ticket_quantity_sold'
                ]
        }),
        ('Location', {
            'fields': [
                'street_address',
                'city',
                'state',
                'country'
                ]
        }),
        ('Slug', {'fields': ['slug']}),
        ('Date & Time', {
            'fields': ['start_time', 'end_time']
        }),
        ('Filters', {
            'fields': ['is_published', 'is_featured']
        }),
    )

    list_display = [
        'name',
        'category',
        'ticket_price',
        'ticket_price',
        'city',
        'state',
        'start_time',
        'end_time',
        'is_published',
        'is_featured',
    ]

    search_fields = [
        'name',
        'description'
        'category',
        'city',
        'state',
    ]

    list_editable = ['is_published', 'is_featured']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(EventCategory)
admin.site.register(EventCity)
admin.site.register(EventState)
admin.site.register(Event, EventAdmin)
admin.site.register(FAQ)
admin.site.register(ContactUs)
admin.site.register(Profile)