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
            'phone': forms.TextInput(attrs={'placeholder': '+8801xxxxxxxxx'})
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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user and user.is_authenticated:
            self.fields.pop('first_name')
            self.fields.pop('last_name')
            self.fields.pop('dob')
            self.fields.pop('gender')
            self.fields.pop('address')
            self.fields.pop('email')
            self.fields.pop('phone')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', '').strip()

        phone = ''.join(filter(str.isdigit, phone))

        if phone.startswith('880'):
            phone = '+' + phone
        elif phone.startswith('0'):
            phone = '+88' + phone[1:]
        elif not phone.startswith('+88'):
            phone = '+88' + phone

        return phone
