from django.contrib.auth import authenticate
from .models import user,Leader
from rest_framework import serializers
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ('id','username', 'email', 'first_name', 'last_name', 'is_leader','password','itinerary','phone_number','avatar')

class LeaderCreationSerializer(serializers.Serializer):
    nationalID=serializers.CharField()
    has_car=serializers.BooleanField()
    car_capacity=serializers.CharField(allow_blank=True)
    car_model=serializers.CharField(allow_blank=True)
    gender=serializers.BooleanField()
    age=serializers.IntegerField()

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'

class LeadPlaceSerializer(serializers.Serializer):
    placeID=serializers.IntegerField()