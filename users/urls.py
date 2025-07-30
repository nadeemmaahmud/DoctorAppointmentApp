from django.urls import path
from .views import user_logout, user_login, user_register, userprofile, userupdate, appointments, change_password, verify_phone, verify_email, verify_phone_otp, verify_email_otp, reset_pass_otp, verify_reset_otp, reset_password_form

urlpatterns = [
    path('login/', user_login, name='login'),
    path("logout/", user_logout, name='logout'),
    path("register/", user_register, name='register'),
    path('profile/', userprofile, name='profile'),
    path('profile/update/', userupdate, name='update'),
    path('profile/change-password/', change_password, name='change_password'),
    path('verify/phone/', verify_phone, name='send_phone_otp'),
    path('verify/phone/otp/', verify_phone_otp, name='verify_phone_otp'),
    path('verify/email/', verify_email, name='send_email_otp'),
    path('verify/email/otp/', verify_email_otp, name='verify_email_otp'),
    path('reset-password/', reset_pass_otp, name='reset_pass'),
    path('reset-password/verify-otp/', verify_reset_otp, name='verify_reset_otp'),
    path('reset-password/new/', reset_password_form, name='reset_password_form'),
    path('appointments/', appointments, name='user_appointments')
]