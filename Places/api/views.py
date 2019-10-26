from django.db.models import Q
from rest_framework.generics import CreateAPIView
from Places.models import Places
from .serializers import CreatePlaceSerializer,ViewPlaceSerializer,ViewPlaceSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

class CreatePlaceAPIView(CreateAPIView):
    queryset = Places.objects.all()
    serializer_class=CreatePlaceSerializer
    serializer_class1=PlaceImageSerializer


class ViewPlaceAPI(generics.ListAPIView):
    queryset = Places.objects.all()
    serializer_class=ViewPlaceSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    search_fields = ['City', 'title']
