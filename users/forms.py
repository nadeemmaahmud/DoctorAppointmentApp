from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    dob = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'dob', 'gender', 'email', 'country_code', 'phone', 'address']

        widgets = {
            'country_code': forms.TextInput(attrs={'placeholder': '+88'}),
            'phone': forms.TextInput(attrs={'placeholder': '01xxxxxxxxx'})
        }
        
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'dob': 'Date of birth',
            'gender': 'Gender',
            'email': 'Email (optional)',
            'phone': 'Phone Number',
        }

    def clean(self):
        cleaned_data = super().clean()
        code = cleaned_data.get('country_code')
        number = cleaned_data.get('phone')

        if code and number:
            merged_phone = f"{code.strip()}{number.strip()}"
            cleaned_data['phone'] = merged_phone
        return cleaned_data

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'dob', 'gender', 'email', 'phone', 'address', 'profile_pic']

        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'})
        }
    
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
