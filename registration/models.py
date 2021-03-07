from django.db import models

# Create your models here.

class ContactUs(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.CharField(max_length=250)
    message =  models.TextField()
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = "ContactUs"
        verbose_name_plural = "ContactUs"

    def __str__(self):
        return f"{self.first_name} {self.first_name} - Contact Query"

