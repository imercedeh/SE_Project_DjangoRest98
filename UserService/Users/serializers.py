from django.contrib.auth import authenticate
from .models import user,Leader
from rest_framework import serializers
from Places.models import Places

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
        fields = ('id','username', 'email', 'first_name', 'last_name', 'is_leader','password','itinerary','phone_number','avatar')

class LeaderCreationSerializer(serializers.Serializer):
    nationalID=serializers.CharField()
    has_car=serializers.BooleanField()
    car_capacity=serializers.CharField(allow_blank=True)
    car_model=serializers.CharField(allow_blank=True)
    gender=serializers.BooleanField()
    age=serializers.CharField()

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Places
        fields=[
            'id',
            'title',
            'image1',
        ]

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'

class LeadPlaceSerializer(serializers.Serializer):
    placeID=serializers.IntegerField()

class SpecificSerializer(serializers.Serializer):
    objID=serializers.IntegerField()

class PlaceLeader(serializers.ModelSerializer):
    class Meta:
        model=Leader
        fields=[
            'userID'
        ]
