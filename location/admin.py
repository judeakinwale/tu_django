from django.contrib import admin
from .models import Listing, ListingCategory, Realtor

# Register your models here.
admin.site.register(Listing)
admin.site.register(ListingCategory)
admin.site.register(Realtor)