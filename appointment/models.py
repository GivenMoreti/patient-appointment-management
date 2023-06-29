from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.user.username


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    
    
    def __str__(self):
        return f"Appointment with {self.doctor.user.username} on {self.date} at {self.time}"
