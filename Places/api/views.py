from django.db.models import Q
from rest_framework.generics import CreateAPIView
from .serializers import CreatePlaceSerializer
from Places.models import Places
from .serializers import CreatePlaceSerializer,PlaceImageSerializer
from rest_framework import status
from rest_framework.response import Response

class CreatePlaceAPIView(CreateAPIView):
    queryset = Places.objects.all()
    serializer_class=CreatePlaceSerializer
    serializer_class1=PlaceImageSerializer