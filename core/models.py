from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.


class Event(models.Model):
    creator =  models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)

    # Create a default category (like Uncategorized or Unknown) as the first category. Deleting it will cause errors
    category = models.ForeignKey("EventCategory", default=1, on_delete=models.SET_DEFAULT)

    # Ticket details
    ticket_price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    ticket_sale_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    ticket_quantity = models.IntegerField(verbose_name="Quantity", default=50)
    ticket_quantity_sold = models.IntegerField(verbose_name="Quantity Sold", default=0)

    # Locaton details
    street_address = models.CharField(max_length=500)
    city = models.ForeignKey("EventCity", on_delete=models.SET_NULL, blank=True, null=True)
    state = models.ForeignKey("EventState", on_delete=models.SET_NULL, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)

    slug = models.SlugField(unique=True)

    # Date and time details
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    is_published = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:event_detail", kwargs={"slug": self.slug})

    def get_event_duration(self):
        if self.end_time:
            return self.start_time - self.end_time
        else:
            return "Unavailable"

    def get_price(self):
        if self.ticket_sale_price and self.ticket_sale_price != 0.00:
            return self.ticket_sale_price
        elif self.ticket_price == 0.00:
            return "Free"
        else:
            return self.ticket_price

    def get_price_savings(self):
        if self.ticket_sale_price and self.ticket_sale_price != 0.00:
            return self.ticket_sale_price - self.ticket_sale_price
        else:
            return "None"

    def tickets_remaining(self):
        return self.ticket_quantity - self.ticket_quantity_sold


class EventCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    summary = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class EventCity(models.Model):
    name = models.CharField(max_length=250, unique=True)
    state =  models.ForeignKey("EventState", on_delete=models.SET_NULL, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class EventState(models.Model):
    name = models.CharField(max_length=250, unique=True)
    summary = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States   '

    def __str__(self):
        return self.name


class FAQ(models.Model):
    title = models.CharField(max_length=200)
    solution = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "ContactUs"
        verbose_name_plural = "ContactUs"

    def __str__(self):
        return f"{self.first_name} {self.first_name} - Contact Query"
