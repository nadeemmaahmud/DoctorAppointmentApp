from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("The Phone Number must be set")
        extra_fields.setdefault('is_active', True)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("Superuser must have is_staff=True.")
        if not extra_fields.get('is_superuser'):
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone, password, **extra_fields)

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

    username = None
    role = models.CharField(choices=ROLES, default='patient')
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(choices=GENDER)
    address = models.CharField(max_length=250)
    email_isverified = models.BooleanField(default=False)
    phone = models.CharField(unique=True, max_length=20)
    phone_isverified = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    profile_pic = models.ImageField(null=True, blank=True, upload_to='Profile_Pics')

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email} - {self.phone}"