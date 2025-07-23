from django.urls import path
from .views import home, appointments, payment, payment_status

urlpatterns = [
    path('', home, name='home'),
    path('appointments/', appointments, name='appointments'),
    path('payment/<str:phone>/', payment, name='payment'),
    path('payment-status/<str:phone>/', payment_status, name='payment_status'),
]
