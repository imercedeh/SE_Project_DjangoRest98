from django.db.models import Q
from rest_framework.generics import CreateAPIView
from Places.models import Places
from .serializers import CreatePlaceSerializer,ViewPlaceSerializer,HomePlaces,SpecificSerializer
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
from .filters import *
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from Users.serializers import UserSerializer
from Users.models import user,Leader
from PlaceService.Global_variables import DatabaseServiceURL,PlaceServiceURL
import requests
import sys, json
from django.conf import settings

class CreatePlace(APIView):
    serializer_class=CreatePlaceSerializer

    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            
            title=serializer.data['title']
            response=requests.get(url=DatabaseServiceURL+"Place/GetPlace/",data={'title':title})

            if response.status_code==200:
                content={'detail':'place with this title already exists!'}
                return Response(data=content,status=status.HTTP_400_BAD_REQUEST)

            else:
                files={}
                data=serializer.data
                
                if('image1' in request.FILES):
                    files={'image1':request.FILES['image1']}

                if('image2' in request.FILES):
                    files={'image2':request.FILES['image2']}

                if('image3' in request.FILES):
                    files={'image3':request.FILES['image3']}

                response=requests.post(url=DatabaseServiceURL+"Place/AddPlace/",data=data,files=files)
                return Response(response.json())
        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

  


class ViewPlaceAPI(generics.ListAPIView):
    serializer_class=ViewPlaceSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    search_fields =  ['id','title', 'Likes','categories','Hardness','Time','StartTime','EndTime','City']

class SearchView(generics.ListAPIView):
    filter_backends = (DynamicSearchFilter,)
    queryset = Places.objects.all()
    serializer_class = ViewPlaceSerializer


class UniquePlace(APIView):
    serializer_class=SpecificSerializer


    def post(self,request,format=None):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            objectid=serializer.data['objID']
            response=requests.post(url=str(DatabaseServiceURL)+'Place/GetUniquePlace/',data={'objID':objectid})
            return Response(response.json(encoding=ascii))

class RandomPlaces(APIView):
    serializer_class = HomePlaces
    def get(self,request):
        response=requests.post(url=str(DatabaseServiceURL)+'Place/GetRandomPlace/')
        return Response(response.json(encoding=ascii))


class PlaceAdvanceSearch(viewsets.ModelViewSet):
    __basic_fields = ('id','title', 'Likes','categories','Hardness','Time','StartTime','EndTime','City')
    queryset = Places.objects.all()
    serializer_class = ViewPlaceSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields