from django.urls import path
from .views import *

app_name = 'dsuser'
urlpatterns = [
    path('', user_login, name='user-login'),
    path('out/', user_logout, name='user-logout'),


    # building APIs
    #path('apilogin/', UserAuthentification.as_view(), name='api-login'),


    ]