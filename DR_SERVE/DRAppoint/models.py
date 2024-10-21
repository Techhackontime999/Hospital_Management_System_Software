from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class DRAppoint_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

class Appointment(models.Model):
    pass