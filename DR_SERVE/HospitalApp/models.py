from django.db import models

import uuid

# service model start
# class ServiceCategory(models.Model):
#     """
#     This model represents the category of the service (e.g., OPD, IPD, Surgery).
#     """
#     name = models.CharField(max_length=100, unique=True)
#     description = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.name

# class Service(models.Model):
#     """
#     This model represents specific services provided by the hospital, like OPD consultations,
#     diagnostic tests, or surgery. Each service belongs to a category.
#     """
#     SERVICE_TYPE_CHOICES = [
#         ('outpatient', 'Outpatient (OPD)'),
#         ('inpatient', 'Inpatient (IPD)'),
#         ('emergency', 'Emergency'),
#         ('diagnostic', 'Diagnostic'),
#         ('surgical', 'Surgical'),
#         ('critical_care', 'Critical Care (ICU)'),
#         ('maternity', 'Maternity & Childcare'),
#         ('pharmacy', 'Pharmacy'),
#         ('rehabilitation', 'Rehabilitation'),
#         ('preventive', 'Preventive & Wellness'),
#         ('telemedicine', 'Telemedicine'),
#         ('mental_health', 'Mental Health'),
#         ('palliative', 'Palliative Care'),
#         ('dental', 'Dental Services'),
#         ('blood_bank', 'Blood Bank & Transfusion'),
#         ('ambulance', 'Ambulance Services'),
#         ('nutrition', 'Nutrition & Dietary Services'),
#         ('home_care', 'Home Care Services'),
#         ('specialized', 'Specialized Clinics'),
#         ('radiology', 'Radiology & Imaging'),
#         ('organ_transplant', 'Organ Transplantation'),
#     ]

#     name = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='services')
#     service_type = models.CharField(max_length=50, choices=SERVICE_TYPE_CHOICES)
#     price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Cost of the service")
#     is_available = models.BooleanField(default=True)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"{self.name} ({self.get_service_type_display()})"

# class HospitalService(models.Model):
#     """
#     This model connects hospitals with services. A hospital can offer multiple services.
#     """
#     hospital = models.ForeignKey('Hospital', on_delete=models.CASCADE)
#     service = models.ForeignKey(Service, on_delete=models.CASCADE)
#     availability_status = models.CharField(max_length=20, choices=[('available', 'Available'), ('unavailable', 'Unavailable')], default='available')
#     start_time = models.TimeField(blank=True, null=True)
#     end_time = models.TimeField(blank=True, null=True)

#     def __str__(self):
#         return f"{self.service.name} at {self.hospital.name}"

# class Hospital(models.Model):
#     """
#     The hospital model where all the services are linked.
#     """
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     name = models.CharField(max_length=100)
#     location = models.CharField(max_length=255)
#     contact_number = models.CharField(max_length=15)
#     email = models.EmailField()
#     password = models.CharField(max_length=128) 
#     services = models.ManyToManyField(Service, through=HospitalService, related_name='hospitals')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

# # service model close

from django.contrib.auth.models import User


class HospitalApp_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username
class Hospital_Management(models.Model):
    pass
