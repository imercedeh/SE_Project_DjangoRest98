from django.contrib.auth import authenticate
from .models import user,Leader
from rest_framework import serializers

class SignupSerializer(serializers.Serializer):
    username = serializers.CharField()
    password=serializers.CharField()
    email = serializers.EmailField(allow_blank=True)
    first_name = serializers.CharField(allow_blank=True)
    last_name = serializers.CharField(allow_blank=True)
    itinerary=serializers.CharField(max_length=500,allow_blank=True)
    phone_number=serializers.CharField(max_length=13,allow_blank=True)

    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('username', 'email', 'first_name', 'last_name', 'password','itinerary','phone_number')

class Become_LeaderSerializer(serializers.Serializer):
    nationalID=serializers.IntegerField()
    has_car=serializers.BooleanField()
    car_capacity=serializers.IntegerField(allow_blank=True)
    car_model=serializers.CharField(allow_blank=True)

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = ('nationalID','has_car','car_capacity','car_model' )
