from django.contrib import admin
from .models import Transportation, TransportationCategory, Operator

# Register your models here.

admin.site.register(Transportation)
admin.site.register(TransportationCategory)
admin.site.register(Operator)