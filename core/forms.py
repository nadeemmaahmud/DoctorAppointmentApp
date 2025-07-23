from django.forms import ModelForm
from django import forms
from .models import Appointment
import datetime

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'dob', 'gender', 'address', 'email', 'phone', 'category', 'date', 'shift', 'prev_case']
        widgets = {
            'date': forms.DateInput(
            attrs={
                'type': 'date',
                'min': (datetime.date.today() + datetime.timedelta(days=1)).isoformat(),
                'max': (datetime.date.today() + datetime.timedelta(days=7)).isoformat(),
            }
            ),
            'shift': forms.Select(attrs={'class': 'form-select'}),
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'dob' : 'Date of Birth',
            'gender': 'Gender',
            'address': 'Full Address',
            'email': 'Email (optional)',
            'phone': 'Phone Number',
            'date': 'Appointment Date',
            'category': 'Doctor Type',
            'shift': 'Shift',
            'prev_case': 'Previous Case No.'
        }