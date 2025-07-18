from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AppointmentForm
from .models import Appointment

def home(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your appointment has been successfully booked!')
            return redirect('home')
    else:
        form = AppointmentForm()

    return render(request, 'home.html', {'form': form})

def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})