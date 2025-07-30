from django.forms import ModelForm
from django import forms
from .models import Appointment
from users.models import CustomUser
import datetime

class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['first_name', 'last_name', 'dob', 'gender', 'address', 'email', 'country_code', 'phone', 'category', 'date', 'shift', 'prev_case']
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
            'country_code': forms.TextInput(attrs={'placeholder': '+88'}),
            'phone': forms.TextInput(attrs={'placeholder': '01xxxxxxxxx'})
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
            self.fields.pop('country_code')
            self.fields.pop('phone')

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get('country_code')
        number = cleaned_data.get('phone')

        if code and number:
            merged_phone = f"{code.strip()}{number.strip()}"
            cleaned_data['phone'] = merged_phone
        return cleaned_data
    
class UserDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['role', 'category', 'description']