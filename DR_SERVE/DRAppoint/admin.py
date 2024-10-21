from django.contrib import admin

# Register your models here.
from .models import DRAppoint_Profile,Appointment

admin.site.register(DRAppoint_Profile)
admin.site.register(Appointment)