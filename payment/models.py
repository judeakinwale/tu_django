from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from cart.context_processor import cart_total_amount

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_phone = models.IntegerField(blank=True, null=True)
    cart_id = models.CharField(max_length=50)
    total_price = models.FloatField()
    timestamp = models.DateTimeField(default=datetime.now())
    billing_address = models.ForeignKey("BillingAddress", on_delete=models.CASCADE, blank=True, null=True)
    payment = models.ForeignKey("Payment", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{user} : {cart_id}"

class BillingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=120)
    apartment_address = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    zipcode = models.CharField(max_length=10)

    class Meta:
        verbose_name = "BillingAddress"
        verbose_name_plural = "BillingAddresses"

    def __str__(self):
        return self.user.username


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=150)
    charge_id = models.CharField(max_length=100)
    amount_due = models.FloatField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.user.username


class CustomerInfo(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
