from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'dob', 'gender', 'email', 'phone', 'password']
        widgets = {
            'dob': forms.DateInput(
            attrs={
                'type': 'date',
            }
            ),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'dob' : 'Date of birth',
            'gender' : 'Gender',
            'email': 'Email (optional)',
            'phone': 'Phone Number',
        }