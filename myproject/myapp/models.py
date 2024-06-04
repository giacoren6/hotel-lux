from django.db import models


# Create your models here.

# models.py
from django.db import models

class Booking(models.Model):
    room_type = models.CharField(max_length=200)
    check_in = models.DateField()
    check_out = models.DateField()
    guest_name = models.CharField(max_length=200)
    guest_email = models.EmailField()
    guest_phone = models.CharField(max_length=200)
    guest_address = models.CharField(max_length=200)
    guest_city = models.CharField(max_length=200)
    guest_state = models.CharField(max_length=200)
    guest_zip = models.CharField(max_length=200)
    guest_country = models.CharField(max_length=200)
    guest_message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.guest_name