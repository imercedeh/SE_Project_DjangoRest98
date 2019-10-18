from django.contrib.auth import authenticate
from .models import user
from rest_framework import serializers
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('username', 'email', 'first_name', 'last_name', 'password','itinerary','phone_number')
