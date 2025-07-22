from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import RegisterForm

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