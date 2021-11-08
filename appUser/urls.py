from django.urls import path
from .views import *

app_name = 'dsuser'
urlpatterns = [
    path('', user_login, name='user-login'),
    path('signup', user_signup, name='user-signup'),
    path('out/', user_logout, name='user-logout'),
    path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),


    # building APIs
    #path('apilogin/', UserAuthentification.as_view(), name='api-login'),


    ]