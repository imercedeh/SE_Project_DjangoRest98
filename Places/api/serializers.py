from rest_framework.serializers import *
from Places.models import Places
from Users.models import user,Leader
from Users.serializers import UserSerializer,LeaderSerializer
from rest_framework import serializers
from django.db.models import Avg

class CreatePlaceSerializer(ModelSerializer):
    class Meta:
        model=Places
        fields = [
        'id',
        'leader',
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
    leader=LeaderSerializer(read_only=True,many=True)
    class Meta:
        model=Places
        fields='__all__' 


class HomePlaces(ModelSerializer):
    class Meta:
        model=Places
        fields=[
            'id',
            'title',
            'image1',
            'categories'   
        ]