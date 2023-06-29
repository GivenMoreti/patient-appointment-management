
from .models import Appointment
from django.shortcuts import render, redirect
from .forms import AppointmentForm
# Create your views here.


def home(request):
    appointment = Appointment.objects.all()
    context = {"appointment": appointment}
    return render(request, "appointment/index.html", context)


def add_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or appointment list
            return redirect('home')
    else:
        form = AppointmentForm()

    context = {
        'form': form
    }
    return render(request, 'appointment/add_appointment.html', context)
