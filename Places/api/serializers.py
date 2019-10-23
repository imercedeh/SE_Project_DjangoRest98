from rest_framework.serializers import ModelSerializer,Serializer
from Places.models import Places


class CreatePlaceSerializer(ModelSerializer):
    class Meta:
        model=Places
        fields=[
            'Title',
            'Image',
            'Description'
        ]