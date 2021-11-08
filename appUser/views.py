from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework import generics


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('ds:dashboard')
            else:
                messages.error(request, 'Wrong username or password!')
                return redirect('dsuser:user-login')
        else:
            messages.error(request, 'Wrong username or password!')
            return redirect('dsuser:user-login')

    return render(request, 'login.html')


def user_logout(request):
    # todo
    pass

class UserAuthentification(): # generics.RetrieveUpdateAPIView
    # todo
    pass