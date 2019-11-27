from django.contrib.auth import authenticate
from .models import TravelLouge
from rest_framework import serializers
from Places.models import Places

class TravelLougeCreationSerializer(serializers.Serializer):
    title = serializers.CharField(allow_blank=True,max_length=102)
    description = serializers.CharField(allow_blank=True,max_length=1000)
    places=serializers.ListField(child=serializers.IntegerField(),allow_empty=True)

class TravellougeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelLouge
        fields = '__all__'