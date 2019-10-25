from rest_framework.serializers import *
from Places.models import Places,PlaceImage
from rest_framework import serializers
from django.db.models import Avg

class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ('image',)


class CreatePlaceSerializer(ModelSerializer):
    images = PlaceImageSerializer(source='placeimage_set', many=True, read_only=True)
    Average1=Places.objects.all().aggregate(Avg('Likes'))
    class Meta:
        model=Places
        fields = [
        'id',
        'title', 
        'images',
        'Description',
        'Likes',
        'categories',
        'Hardness',
        'Address',
        'Time',
        'City',
        'Average',
        ]
        read_only_fields = ('Average',)



    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        places = Places.objects.create(
        title=validated_data.get('title', 'no-title'),
        Description=validated_data.get('Description'),
        Likes=validated_data.get('Likes'),
        categories=validated_data.get('categories'),
        Hardness=validated_data.get('Hardness'),
        Address=validated_data.get('Address'),
        Time=validated_data.get('Time'),
        City=validated_data.get('City'),
        Average=Places.objects.all().aggregate(Avg('Likes'))
        ,)

        for image_data in images_data.values():
            PlaceImage.objects.create(places=places, image=image_data)
        
        return places

class ViewPlaceSerializer(ModelSerializer):
    class Meta:
        model=Places
        fields='__all__' 