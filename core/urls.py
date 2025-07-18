from django.urls import path
from .views import home, appointments

urlpatterns = [
    path('', home, name='home'),
    path('appointments/', appointments, name='appointments'),
]
