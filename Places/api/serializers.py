from rest_framework.serializers import *
from Places.models import Places,Comment
from Users.models import user,Leader
from Users.serializers import UserSerializer,LeaderSerializer,PlaceLeader
from rest_framework import serializers
from django.db.models import Avg


class SpecificSerializer(serializers.Serializer):
    objID=serializers.IntegerField()

class CreatePlaceSerializer(ModelSerializer):
    image1=SerializerMethodField()
    image2=SerializerMethodField()
    image3=SerializerMethodField()
    #Likes=SerializerMethodField()
    #Average=SerializerMethodField()
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

    def get_image1(self, obj):
        try:
            image = "http://127.0.0.1:8000"+obj.image1.url
        except:
            image = None
        return image

    def get_image2(self, obj):
        try:
            image = "http://127.0.0.1:8000"+obj.image1.url
        except:
            image = None
        return image

    def get_image3(self, obj):
        try:
            image = "http://127.0.0.1:8000"+obj.image1.url
        except:
            image = None
        return image

    # def get_Average(self,obj):
    #     likes=obj.Likes
    #     #likes=Places.objects.get(likes=obj.Likes)
    #     return likes/obj.id.count()



class ViewPlaceSerializer(ModelSerializer):
    #pp=uuSerializer(read_only=True)
    #leader=PlaceLeader(read_only=True)
    image1=SerializerMethodField()
    class Meta:
        model=Places
        #fields='__all__' 
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

    def get_image1(self, obj):
        try:
            image = "http://127.0.0.1:8000"+obj.image1.url
        except:
            image = None
        return image


class HomePlaces(ModelSerializer):
    class Meta:
        model=Places
        fields=[
            'id',
            'title',
            'image1',
            'categories'   
        ]


class CommentSerializer(ModelSerializer):
    class Meta:
        model=Comment
        fields=[
            'comment',
            'user',
            'place',
        ]