from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

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