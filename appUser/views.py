from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.cache import cache_control


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


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def user_logout(request):
    logout(request)
    return redirect('dsuser:user-login')



# make APIs
class UserAuthentification(): # generics.RetrieveUpdateAPIView
    # todo
    pass