import datetime

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views import View

from .models import Profile, Poke
from .tokens import account_activation_token
from django.views.decorators.cache import cache_control
from .forms import SignUpForm

# Create your views here.


def user_login(request):
    if request.method == 'GET' and request.user and request.user.is_active:
        return redirect('dsuser:campdashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request=request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('dsuser:campdashboard')
            else:
                messages.error(request, 'User is not Active anymore!')
                return redirect('dsuser:user-login')
        else:
            messages.error(request, 'Wrong username or password!')
            return redirect('dsuser:user-login')
    return render(request, 'login.html')


def user_signup(request):
    form = SignUpForm(request.POST)
    context = {'form': form}
    if request.method == 'GET':
        return render(request, 'signup.html', context=context)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        print(form.error_messages)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate account till it is confirmed
            user.is_superuser = False
            user.is_staff = False
            print(type(form.cleaned_data['date']),form.cleaned_data['date'])
            user.save()
            user.profile.birthdate = form.cleaned_data['date']

            user.profile.save()

            #current_site = get_current_site(request)
            #subject = 'Activate Your MySite Account'
            #message = render_to_string('account_activation_email.html', {
            #    'user': user,
            #    'domain': current_site.domain,
            #    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #    'token': account_activation_token.make_token(user),
            #})
            #user.email_user(subject, message)
            messages.success(request, 'Please Confirm your email to complete registration.')
            return redirect('dsuser:user-login')
        else:
            context['error'] = form.error_messages

        return render(request, 'signup.html', context=context)


class ActivateAccount(View):
    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            # user.profile.email_confirmed = True
            user.save()
            login(request, user)
            messages.success(request, 'Your account have been confirmed.')
            return redirect('ds:dashboard')
        else:
            messages.warning(request, 'The confirmation link was invalid, possibly because it has already been used.')
            return redirect('dsuser:user-signup')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def user_logout(request):
    logout(request)
    return redirect('dsuser:user-login')


def campdashboard(request):
    pokes = Poke.objects.filter(poked=request.user, viewed=None).all()
    for poke in pokes:
        poke.viewed = datetime.datetime.now()
        poke.save()
    data = {}
    if pokes.count() > 0:
        data['ncount'] = pokes.count()
        data['my_pokes'] = pokes
    return render(request, "campDashboard.html", context=data)

def poke_me(request):
    user = User.objects.get(id=request.GET['prf'])
    poke = Poke(author=request.user, poked=user)
    poke.save()
    return JsonResponse({'pokes':user.profile.pokes()}, status=200)

# make APIs
class UserAuthentification(): # generics.RetrieveUpdateAPIView
    # todo
    pass

