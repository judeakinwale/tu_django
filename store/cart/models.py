from django.db import models
from django.contrib.auth.models import User
from core.models import Event
from payment.models import BillingAddress, Payment

# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    guest_user_session_id =  models.CharField(max_length=200, null=True, blank=True)
    item = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_item_sale_price(self):
        return self.quantity * self.item.sale_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_item_sale_price()

    def get_final_price(self):
        if self.item.sale_price:
            return self.get_total_item_sale_price()
        return self.get_total_item_price()     


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    guest_user_session_id =  models.CharField(max_length=200, null=True, blank=True)
    items = models.ManyToManyField("CartItem")
    start_date = models.DateTimeField(auto_now=False, auto_now_add=True)    
    ordered_date = models.DateTimeField(auto_now=True, null=True, blank=True)
    ordered = models.BooleanField(default=False)
    billing_address = models.ForeignKey(BillingAddress,  on_delete=models.CASCADE, blank=True, null=True)
    payment = models.ForeignKey(Payment,  on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.id}"

    def get_total(self):
        total = 0
        for cart_item in self.items.all():
            total += cart_item.get_final_price( )
        return total
