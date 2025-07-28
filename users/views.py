from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.core.mail import send_mail
from .forms import RegisterForm, UserProfileForm
from core.models import Appointment
from django.conf import settings
from twilio.rest import Client
import random

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            phone = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=phone, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "You've been logged in!")
                return redirect('home')
            else:
                messages.error(request, "Invalid login!")
                return redirect('login')
    else:
        form = AuthenticationForm()

    return render(request, "login_register_form.html", {'form':form})

def user_logout(request):
    logout(request)
    messages.success(request, "You've been logged out!")
    return redirect('home')

def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "You've been successfully registered! Please login to continue.")
            return redirect('login')
    else:
        form = RegisterForm()

    return render(request, "login_register_form.html", {'form':form, 'create':True})

def userupdate(request):
    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=request.user, user=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated!")
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user, user=request.user)

    return render(request, "update_profile.html", {'form': form})

def userprofile(request):
    userdata = request.user
    return render(request, "user_profile.html", {'userdata': userdata})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_reset_password.html', {'form': form, 'update': True})

def verify_phone(request):
    if request.method == 'POST':
        code = str(random.randint(100000, 999999))
        request.session['phone_otp'] = code
 
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
        twilio_message = client.messages.create(
            body=f"Your verification code is {code}",
            from_=settings.TWILIO_PHONE_NUMBER,
            to=request.user.phone
        )
            
        messages.success(request, "Verification code sent!")
        return redirect('verify_phone_otp')
        
    return render(request, 'otp_check.html')

def verify_email(request):
    if request.method == 'POST':
        otp = str(random.randint(100000, 999999))
        request.session['email_otp'] = otp

        subject = 'Email Verification Code'
        message = f'Your email verification code is: {otp}'
        from_email = settings.DEFAULT_FROM_EMAIL
        to_email = request.user.email

        send_mail(subject, message, from_email, [to_email])
        messages.success(request, 'Verification code sent to your email.')
        return redirect('verify_email_otp')
            
    return render(request, 'otp_check.html')
        
def verify_phone_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        real_otp = request.session.get('phone_otp')

        if entered_otp == real_otp:
            user = request.user
            user.phone_isverified = True
            user.save()
            del request.session['phone_otp']
            messages.success(request, "Phone number verified!")
            return redirect('profile')
        else:
            messages.error(request, "Incorrect verification code.")

    return render(request, 'verify_otp.html')

def verify_email_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        real_otp = request.session.get('email_otp')

        if entered_otp == real_otp:
            request.user.email_isverified = True
            request.user.save()
            del request.session['email_otp']
            messages.success(request, "Email verified successfully.")
            return redirect('profile')
        else:
            messages.error(request, "Incorrect verification code.")

    return render(request, 'verify_email_otp.html')


def appointments(request):
    appointment = Appointment.objects.filter(phone=request.user.phone)
    return render(request, 'appointments.html', {'appointments': appointment})