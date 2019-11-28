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
    serializer_class=ViewPlaceSerializer
    #filter_class = PlacesFilter
    filter_backends= [SearchFilter, OrderingFilter]
    search_fields =  ['id','title', 'Likes','categories','Hardness','Time','StartTime','EndTime','City']

    def get_queryset(self,*args,**kwargs):
        queryset_list = Places.objects.all()
        query=self.request.GET.get('q')
        if query is not None:
            queryset_list=queryset_list.filter(
                Q(id__iexact=query)|
                Q(title__iexact=query)|
                Q(Likes__iexact=query)|
                Q(categories__iexact=query)|
                Q(Hardness__iexact=query)|
                Q(Time__iexact=query)|
                Q(StartTime__iexact=query)|
                Q(EndTime__iexact=query)|
                Q(City__iexact=query)
            ).distinct()
        return queryset_list

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