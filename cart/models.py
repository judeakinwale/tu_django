from django.db import models
from django.shortcuts import redirect, reverse
from core.models import Event

# Create your models here.


class CartItem(models.Model):
    cart = models.ForeignKey("Cart", on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    line_total = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        try:
            return str(self.cart.id)
        except:
            return self.event.name

    # def get_absolute_url(self):
    #     return reverse("Cart_detail", kwargs={"pk": self.pk})

class Cart(models.Model):
    total = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f"Cart Id: {self.id}"
    
