from django.contrib import admin
from myapp.models import Booking

# Register your models here.

admin.site.site_header = "Hotel Booking Admin"
admin.site.site_title = "Hotel Booking Admin Portal"
admin.site.index_title = "Welcome to Hotel Booking Portal"

admin.site.register(Booking)
