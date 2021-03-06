from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from django.shortcuts import reverse
# from datetime import datetime
from core.models import EventState, EventCity

# Create your models here.


class Transportation(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(verbose_name="Price per day", max_digits=10, decimal_places=2)
    phone = models.CharField(max_length=200, blank=True, null=True)

    # Vehicle details
    capacity = models.IntegerField()
    vehicle_type = models.ForeignKey(
        "TransportationCategory",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
        )

    # Vehicle location details
    city = models.ForeignKey(EventCity, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(EventState, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)

    # Vehicle images
    photo_main = models.ImageField(upload_to='images/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    # Filters
    is_published = models.BooleanField(default=True)
    is_booked = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Transportation"
        verbose_name_plural = "Transportation"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("transportation:transportation_detail", kwargs={"pk": self.pk})


class TransportationCategory(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "Vehicle Type"
        verbose_name_plural = "Vehicle Types"

    def __str__(self):
        return self.name
