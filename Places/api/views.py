from django.db.models import Q
from rest_framework.generics import CreateAPIView
from Places.models import Places
from .serializers import CreatePlaceSerializer,ViewPlaceSerializer,HomePlaces
from rest_framework import generics
from django.http import Http404
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser


class CreatePlaceAPIView(CreateAPIView):
    queryset = Places.objects.all()
    serializer_class=CreatePlaceSerializer
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser)


class ViewPlaceAPI(generics.ListAPIView):
    queryset = Places.objects.all()
    serializer_class=ViewPlaceSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    search_fields = ['City', 'title']


class UniquePlaceAPI(generics.ListAPIView):
    queryset=Places.objects.all()
    serializer_class=ViewPlaceSerializer
    filter_backends= [SearchFilter]
    search_fields = ['id']
    
    def get_queryset(self):
        queryset = Places.objects.all()
        id = self.request.query_params.get('search')
        if id is not None:
             queryset = queryset.filter(id__exact=id).distinct()
        return queryset


class RandomPlaces(generics.ListAPIView):
    queryset = Places.objects.all().order_by('?')[:3]
    serializer_class = HomePlaces


class PlaceAdvanceSearch(viewsets.ModelViewSet):
    __basic_fields = ('id','title', 'Likes','categories','Hardness','Time','StartTime','EndTime','City')
    queryset = Places.objects.all()
    serializer_class = ViewPlaceSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields