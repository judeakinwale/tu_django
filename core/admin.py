from django.contrib import admin
from .models import Event, EventCategory, EventCity, EventState, FAQ

# Register your models here.


# @admin.register()
class EventAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ['creator','name', 'category', 'description', 'image'],
        }),
        ('Price', {'fields': ['price', 'sale_price']}),
        ('Location', {'fields': ['location', 'city', 'state', 'country']}),
        ('Slug', {'fields': ['slug']}),
        ('Date & Time', {'fields': ['start_time', 'end_time']}),
        ('Misc', {'fields': ['active', 'featured']}),
    )

    list_display = ['name', 'category', 'price', 'start_time', 'active', 'featured']
    list_editable = ['active', 'featured']
    prepopulated_fields = {'slug': ('name',)}




admin.site.register(EventCategory)
admin.site.register(EventCity)
admin.site.register(EventState)
admin.site.register(Event, EventAdmin)
admin.site.register(FAQ)