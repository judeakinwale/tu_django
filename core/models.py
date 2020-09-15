from django.db import models

# Create your models here.

EVENT_CHOICES = {
    ('S', 'Seminars'),
    ('C', 'Conferences'),
    ('TS', 'Trade Shows'),
    ('W', 'Workshops'),
    ('R', 'Reunions'),
    ('P', 'Parties'),
    ('G', 'Galas'),
    ('WE', 'Webinars'),
    ('I', 'Internet Streams'),
    ('U', 'Uncategorized'),
}


class Event(models.Model):
    name = models.CharField(max_length=250)
    category = models.CharField(choices=EVENT_CHOICES, max_length=3, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
    location = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    sale_price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) 
    # country =
    # state = 
    # city = 
    slug = models.SlugField(unique=True)
    start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    end_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    updated = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    

    class Meta:
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("event_detail", kwargs={"slug": self.slug})

    def get_event_duration(self):
        return self.start_time - self.end_time

    
