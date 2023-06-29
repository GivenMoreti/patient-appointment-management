from django.contrib import admin
from .models import Patient,Doctor,Appointment
# Register your models here.

class PatientModel(admin.ModelAdmin):
    list_display = ("user","date_of_birth","phone_number")

class DoctorModel(admin.ModelAdmin):
    list_display = ("user","specialization")

class AppointmentModel(admin.ModelAdmin):
    list_display = ("doctor","patient","date","time")



admin.site.register(Patient,PatientModel)
admin.site.register(Doctor,DoctorModel)
admin.site.register(Appointment,AppointmentModel)