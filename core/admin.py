from django.contrib import admin
from .models import Event, EventCategory

# Register your models here.


# @admin.register()
class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['name', 'category', 'description'],
        }),
        ('Price', {'fields': ['price', 'sale_price']}),
        ('Location', {'fields': ['location']}),
        ('Slug', {'fields': ['slug']}),
        ('Date & Time', {'fields': ['start_time', 'end_time']}),
        ('Misc', {'fields': ['active', 'featured']}),
    )
    
    list_display = ['name', 'category', 'price', 'start_time', 'active']
    prepopulated_fields = {'slug': ('name',)}
    # fields = []


    
admin.site.register(EventCategory)
admin.site.register(Event, EventAdmin)