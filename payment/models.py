from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

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