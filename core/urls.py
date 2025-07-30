from django.urls import path
from .views import home, appointments, payment, payment_status, users, user_details, appointment_detailes

urlpatterns = [
    path('', home, name='home'),
    path('appointments/', appointments, name='appointments'),
    path('appointment-details/<int:pk>/', appointment_detailes, name='appointment_details'),
    path('payment/<str:phone>/', payment, name='payment'),
    path('payment-status/<str:phone>/', payment_status, name='payment_status'),
    path('users/', users, name='users'),
    path('users/<int:pk>/', user_details, name='user_details'),
]
