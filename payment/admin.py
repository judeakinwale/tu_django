from django.contrib import admin
from .models import  BillingAddress, Payment

# Register your models here.

admin.site.register(BillingAddress)
admin.site.register(Payment)
