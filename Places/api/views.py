from django.db.models import Q
from rest_framework.generics import CreateAPIView
from Places.models import Places
from .serializers import CreatePlaceSerializer,ViewPlaceSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


class CreatePlaceAPIView(CreateAPIView):
    queryset = Places.objects.all()
    serializer_class=CreatePlaceSerializer
    parser_classes = (MultiPartParser, FormParser)


class ViewPlaceAPI(generics.ListAPIView):
    queryset = Places.objects.all()
    serializer_class=ViewPlaceSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    search_fields = ['City', 'title']


class UniquePlaceAPI(generics.ListAPIView):
    queryset=Places.objects.all()
    serializer_class=ViewPlaceSerializer
    serializer_class1=PlaceImageSerializer
    filter_backends= [SearchFilter]
    search_fields = ['id']
    
    def get_queryset(self):
        queryset = Places.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(Places__id=id)
        return queryset
