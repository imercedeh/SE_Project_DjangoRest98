from django.contrib.auth import authenticate
from .models import user,Leader
from rest_framework import serializers
from Places.models import Places


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields ='__all__'

class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leader
        fields = '__all__'
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model=Places
        fields=fields = '__all__'