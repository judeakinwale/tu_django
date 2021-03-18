from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import datetime
from cart.context_processor import cart_total_amount
from core.models import Event

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_phone = models.IntegerField(blank=True, null=True)
    cart_id = models.CharField(max_length=50)
    total_price = models.FloatField()
    timestamp = models.DateTimeField(default=datetime.now)
    billing_address = models.ForeignKey("BillingAddress", on_delete=models.CASCADE, blank=True, null=True)
    payment = models.ForeignKey("Payment", on_delete=models.CASCADE, blank=True, null=True)
    is_ordered = models.BooleanField(default=False)

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
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


class UserOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    ticket_id = models.CharField(max_length=50, blank=True, null=True)
    ticket_name = models.CharField(max_length=250, blank=True, null=True)
    ticket_email = models.CharField(max_length=500, blank=True, null=True)
    user_phone = models.IntegerField(blank=True, null=True)
    order_items = models.ManyToManyField(Event, blank=True)
    cart_id = models.CharField(max_length=200, blank=True, null=True)
    order_item_qty = models.CharField(max_length=200, blank=True, null=True)
    amount_due = models.FloatField(blank=True, null=True)
    is_ordered = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class PaymentConfirmation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    sender = models.CharField(max_length=200, blank=True, null=True)
    user_order = models.ForeignKey(UserOrder, on_delete=models.CASCADE, blank=True, null=True)
    reference = models.CharField(max_length=200, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    raw_request = models.TextField(blank=True, null=True)
    event = models.CharField(max_length=200, blank=True, null=True)
    data = models.CharField(max_length=500, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)


class CreatorPayment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # Tickets sold at payment
    tickets_sold = models.IntegerField()
    tickets_remaining = models.IntegerField()
    tickets_paid_for = models.IntegerField()
    tickets_total = models.IntegerField()

    payment_id = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("CreatorPayment_detail", kwargs={"pk": self.pk})

    def tickets_to_be_paid_for(self):
        return self.tickets_sold - tickets_paid_for
