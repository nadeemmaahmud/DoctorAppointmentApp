from django.forms import ModelForm
from django import forms
from .models import Appointment
import datetime

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'email', 'phone', 'date', 'shift']
        widgets = {
            'date': forms.DateInput(
            attrs={
                'type': 'date',
                'min': (datetime.date.today() + datetime.timedelta(days=1)).isoformat(),
                'max': (datetime.date.today() + datetime.timedelta(days=7)).isoformat(),
            }
            ),
            'shift': forms.Select(attrs={'class': 'form-select'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'email': 'Email (optional)',
            'phone': 'Phone Number',
            'date': 'Appointment Date',
            'shift': 'Shift',
        }