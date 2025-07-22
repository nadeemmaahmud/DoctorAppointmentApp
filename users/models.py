from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class CustomUser(AbstractUser):
    ROLES = [
        ('admin', 'Admin'),
        ('doctor', 'Doctor'),
        ('patient', 'Patient')
    ]
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    role = models.CharField(choices=ROLES, default='patient')
    dob = models.DateField()
    gender = models.CharField(choices=GENDER)
    email_isverified = models.BooleanField(default=False)
    phone = models.CharField(unique=True, max_length=20)
    phone_isverified = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='Profile_Pics')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} - {self.phone}"