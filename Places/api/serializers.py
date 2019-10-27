from rest_framework.serializers import *
from Places.models import Places
from rest_framework import serializers
from django.db.models import Avg

class CreatePlaceSerializer(ModelSerializer):
    class Meta:
        model=Places
        fields = [
        'id',
        'title', 
        'image1',
        'image2',
        'image3',
        'Description',
        'Likes',
        'categories',
        'Hardness',
        'Address',
        'Time',
        'StartTime',
        'EndTime',
        'City',
        'Average',
        ]
        read_only_fields = ('Average',)



class ViewPlaceSerializer(ModelSerializer):
    class Meta:
        model=Places
        fields='__all__' 