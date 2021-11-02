from django.urls import path
from .views import *

app_name = 'ds'
urlpatterns = [
    path('', dashboard, name='dashboard'),


    # building APIs
    path('projectlist/', DSProjectList.as_view(), name='prl'),


    ]