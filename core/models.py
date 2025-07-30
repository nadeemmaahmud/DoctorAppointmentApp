from django.db import models
from users.models import Category

class Appointment(models.Model):
    GENDER = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ]

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    dob = models.DateField()
    gender = models.CharField(max_length=20, choices=GENDER)
    address = models.CharField(max_length=250)
    email = models.EmailField(max_length=50, blank=True, null=True)
    country_code = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    shift = models.CharField(max_length=20, choices=[('morning-9am', 'Morning - 9AM'), ('afternoon-3pm', 'Afternoon - 3PM'), ('evening-7pm', 'Evening - 7PM')])
    prev_case = models.CharField(max_length=10, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    is_postponded = models.BooleanField(default=False)
    initial_real_disease = models.TextField(null=True, blank=True)
    testes = models.TextField(null=True, blank=True)
    pescription = models.TextField(null=True, blank=True)
    check_again = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Case No. {self.id} : {self.first_name} {self.last_name} | {self.date} | {self.shift}"
    
