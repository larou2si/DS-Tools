from django.shortcuts import render
from rest_framework import generics
from .serializers import DSProject, DSProjectSerializer
# Create your views here.

def dashboard(request):
    return render(request, 'index.html')

class DSProjectList(generics.ListCreateAPIView):
    queryset = DSProject.objects.using('users_db').all()
    serializer_class = DSProjectSerializer

