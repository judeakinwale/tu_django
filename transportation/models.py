from django.db import models
from datetime import datetime

# Create your models here.


class Transportation(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey("TransportationCategory", verbose_name="Category", on_delete=models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    capacity = models.IntegerField()
    price = models.DecimalField(verbose_name="Price per day", max_digits=10, decimal_places=2)
    country = models.CharField(max_length=200, blank=True, null=True) 
    state = models.CharField(max_length=200, blank=True, null=True)  
    city = models.CharField(max_length=200, blank=True, null=True)  
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    list_date = models.DateTimeField(default=datetime.now)
    is_published = models.BooleanField(default=True)
    is_booked = models.BooleanField(default=False)


    class Meta:
        verbose_name = "Transportation"
        verbose_name_plural = "Transportation"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # return reverse("transportation_detail", kwargs={"pk": self.pk})
        pass


class TransportationCategory(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    timestamp = models.DateTimeField(default=datetime.now)
    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
