from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    dob = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'dob', 'gender', 'email', 'phone']
        widgets = {
            
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'dob': 'Date of birth',
            'gender': 'Gender',
            'email': 'Email (optional)',
            'phone': 'Phone Number',
        }