from django.contrib import admin
from .models import  BillingAddress, Payment, CustomerInfo, Order

# Register your models here.

admin.site.register(BillingAddress)
admin.site.register(Payment)
admin.site.register(CustomerInfo)
admin.site.register(Order)