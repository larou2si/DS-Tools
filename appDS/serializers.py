from rest_framework import serializers
from .models import DSProject

class DSProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = DSProject
        fields = '__all__'
