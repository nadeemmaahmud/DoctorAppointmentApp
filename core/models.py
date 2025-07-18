from django.db import models

class Appointment(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    email = models.EmailField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=15)
    date = models.DateField()
    shift = models.CharField(max_length=10, choices=[('morning', 'Morning'), ('afternoon', 'Afternoon'), ('evening', 'Evening')])

    def __str__(self):
        return f"Case No. {self.id} : {self.first_name} {self.last_name} | {self.date} | {self.shift}"
    
