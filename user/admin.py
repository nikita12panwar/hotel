from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header = "Hotel Raj Admin"
admin.site.register(Usersignup)
admin.site.register(Adminsignup)
admin.site.register(Booking)
admin.site.register(Room)