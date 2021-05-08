from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.translation import gettext as _
from core.models import EventCity, EventState

# Create your models here.


class Listing(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=300)  # Usually the same as the street address
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    category = models.ForeignKey("ListingCategory", on_delete=models.SET_NULL, blank=True, null=True)

    # Building / apartment details
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=10, decimal_places=1)
    pools = models.IntegerField()
    lot_size = models.DecimalField(max_digits=10, decimal_places=1, blank=True, null=True)

    # Images of the listing
    photo_main = models.ImageField(upload_to='images/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)
    photo_6 = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True, null=True)

    # address details
    street_address = models.CharField(max_length=300)
    city = models.ForeignKey(EventCity, on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey(EventState, on_delete=models.SET_NULL, blank=True, null=True)
    country = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=100, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    # Filters
    is_published = models.BooleanField(default=True)
    is_booked = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("location:location_detail", kwargs={"pk": self.pk})


class ListingCategory(models.Model):
    name = models.CharField(max_length=200)
    summary = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name
