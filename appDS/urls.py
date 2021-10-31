from django.urls import path
from .views import *

app_name = 'ds'
urlpatterns = [
    path('', dashboard, name='dashboard'),

    ]