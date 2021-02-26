from django.db import models
from django.contrib.auth.models import User 
from django.shortcuts import reverse
from django.utils import timezone

# Create your models here.

# EVENT_CHOICES = {
#     ('S', 'Seminars'),
#     ('C', 'Conferences'),
#     ('TS', 'Trade Shows'),
#     ('W', 'Workshops'),
#     ('R', 'Reunions'),
#     ('P', 'Parties'),
#     ('G', 'Galas'),
#     ('WE', 'Webinars'),
#     ('I', 'Internet Streams'),
#     ('U', 'Uncategorized'),
# }


class Event(models.Model):
    creator =  models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    # category = models.CharField(choices=EVENT_CHOICES, max_length=3, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey("EventCategory", verbose_name="Category", default=1, on_delete=models.SET_DEFAULT)
    image = models.ImageField(upload_to="images/%Y/%m/%d/", blank=True, null=True)
    location = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    sale_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True) 
    country = models.CharField(max_length=200, blank=True, null=True) 
    # state = models.CharField(max_length=200, blank=True, null=True)
    # city = models.CharField(max_length=200, blank=True, null=True)
    state = models.ForeignKey("EventState", on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey("EventCity", on_delete=models.SET_NULL, blank=True, null=True)
    slug = models.SlugField(unique=True)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("core:event_detail", kwargs={"slug": self.slug})

    def get_event_duration(self):
        if self.end_time:
            return self.start_time - self.end_time
        else:
            return "unavailable"

    
class EventCategory(models.Model):
    name = models.CharField(max_length=250, unique=True)
    summary = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class EventCity(models.Model):
    name = models.CharField(max_length=250, unique=True)
    state =  models.ForeignKey("EventState", on_delete=models.SET_NULL, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

    def __str__(self):
        return self.name


class EventState(models.Model):
    name = models.CharField(max_length=250, unique=True)
    summary = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'State'
        verbose_name_plural = 'States   '

    def __str__(self):
        return self.name


class FAQ(models.Model):
    title = models.CharField(max_length=200)
    solution = models.TextField()

    def __str__(self):
        return self.title

