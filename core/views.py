import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import login, get_backends
from django.contrib import messages
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from datetime import date
from sslcommerz_python_api import SSLCSession
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from .forms import AppointmentForm
from .models import Appointment

def home(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.is_paid = False  # Mark as unpaid initially
            appointment.save()

            return redirect('payment', phone=appointment.phone)
    else:
        form = AppointmentForm()

    return render(request, 'home.html', {'form': form})

def payment(request, phone):
    mypayment = SSLCSession(
    sslc_is_sandbox=True,
    sslc_store_id=os.environ.get('sslc_store_id'),
    sslc_store_pass=os.environ.get('sslc_store_pass')
    )

    status_url = request.build_absolute_uri(reverse('payment_status', kwargs={'phone': phone}))

    mypayment.set_urls(
    success_url=status_url,
    fail_url=status_url,
    cancel_url=status_url,
    ipn_url=status_url
    )


    mypayment.set_product_integration(
    total_amount=300.00,
    currency='BDT',
    product_category='Patient',
    product_name='Booking an appointment',
    num_of_item=1,
    shipping_method='NO',
    product_profile='None'
    )

    mypayment.set_customer_info(
    name='N/A',
    email='N/A',
    address1='N/A',
    address2='N/A',
    city='N/A',
    postcode='N/A',
    country='N/A',
    phone=phone,
    )

    mypayment.set_shipping_info(
    shipping_to='demo customer',
    address='demo address',
    city='Dhaka',
    postcode='1209',
    country='Bangladesh'
    )

    
    mypayment.set_additional_values(
    #value_a='user.id',
    #value_b='portalcustomerid',
    #value_c='1234',
    #value_d='uuid'
    )

    response_data = mypayment.init_payment()

    gateway_url = response_data.get('GatewayPageURL')
    if gateway_url:
        return redirect(gateway_url)
    else:
        error_message = response_data.get('failedreason', 'Payment gateway initialization failed. Please try again later.')
        return HttpResponse(error_message, status=500)

@csrf_exempt
def payment_status(request, phone):
    if request.method == "POST":
        status = request.POST.get('status')
        
        if status == 'VALID':
            try:
                appointment = Appointment.objects.get(phone=phone, is_paid=False)
                appointment.is_paid = True
                appointment.save()
                messages.success(request, 'Appointment successfully booked after payment!')

                client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
                twilio_message = client.messages.create(
                    body=f"Your appointment is booked for {appointment.date} on {appointment.shift} shift. Please come to the clinic on time.",
                    from_=settings.TWILIO_PHONE_NUMBER,
                    to=appointment.phone
                )
            except Appointment.DoesNotExist:
                print(f"No unpaid appointment found for phone: {phone}")
        else:
            print(f"Payment failed for phone number: {phone}. Status: {status}")
    else:
        print("Invalid request method. Only POST requests are allowed.")

    return redirect('home')

def appointments(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})