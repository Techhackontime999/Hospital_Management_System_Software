
# Create your models here.
# DRFeature/models.py
from django.db import models
from django.contrib.auth.models import User  # Import Django's default User model


class DR_Feature_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.user.username

# class MedicalContent(models.Model):
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     content_file = models.FileField(upload_to='medical_content/')
#     uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'doctor'})
#     upload_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# class Consultation(models.Model):
#     patient = models.ForeignKey(User, related_name='consultations', on_delete=models.CASCADE, limit_choices_to={'user_type': 'patient'})
#     doctor = models.ForeignKey(User, related_name='doctor_consultations', on_delete=models.CASCADE, limit_choices_to={'user_type': 'doctor'})
#     consultation_date = models.DateTimeField()
#     notes = models.TextField()

#     def __str__(self):
#         return f"Consultation: {self.patient} with {self.doctor}"
