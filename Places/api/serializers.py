from rest_framework.serializers import *
from Places.models import Places,PlaceImage

class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ('image',)


class CreatePlaceSerializer(ModelSerializer):
    class Meta:
        model=Places
        fields=[
            'Title',
            'Image',
            'Description'
        ]