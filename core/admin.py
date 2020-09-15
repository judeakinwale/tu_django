from django.contrib import admin
from .models import Event

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
        ('Date & Time', {'fields': ['start_time', 'end_time', 'timestamp', 'updated']}),
        ('Misc', {'fields': ['active', 'featured']}),
    )
    
    list_display = ['name', 'category', 'price', 'timestamp', 'start_time', 'active']
    # fields = []
    


admin.site.register(Event, EventAdmin)