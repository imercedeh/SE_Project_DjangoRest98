from django.shortcuts import render
from .models import TravelLouge
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import TravelLougeCreationSerializer,TravellougeSerializer
from rest_framework import status
from Places.models import Places
from Users.models import user,Leader
from Users.serializers import LeadPlaceSerializer,SpecificSerializer
from TravellougeService.Global_variables import DatabaseServiceURL
import requests
import json


class TravelLougeCreation(APIView):
    serializer_class=TravelLougeCreationSerializer

    def post(self,request):
      
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            
            files={}
            data=serializer.data
            headers=request.headers
            data = json.dumps(request.data)
            # if('image1' in request.data):
            #     name=request.data['name1']
            #     contentType=request.data['content_type1']
            #     avatar=request.data[name]
            #     files={name:avatar.file}
            #     data['image1']='True'
            #     data['content_type1']=contentType
            #     data['name1']=name
            
            # if('image2' in request.data):
            #     name=request.data['name2']
            #     contentType=request.data['content_type2']
            #     avatar=request.data[name]
            #     files={name:avatar.file}
            #     data['image2']='True'
            #     data['content_type2']=contentType
            #     data['name2']=name
            
            # if('image3' in request.data):
            #     name=request.data['name3']
            #     contentType=request.data['content_type3']
            #     avatar=request.data[name]
            #     files={name:avatar.file}
            #     data['image3']='True'
            #     data['content_type3']=contentType
            #     data['name3']=name

            response = requests.post(url=DatabaseServiceURL+"Travellouge/AddTravellouge/",data=data,files=files,headers=headers)
            return Response(response.json())
        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
 

class PlaceTravelLougesAPI(APIView):
    permission_classes=(AllowAny,)
    serializer_class =LeadPlaceSerializer
    serializer_class2=TravellougeSerializer
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            place=Places.objects.get(id=serializer.data['placeID'])
            set=list(place.travellouge_set.all())
            data={}
            data['travellouges']=[]
            for travellouge in set:
                serializer2=self.serializer_class2(travellouge)
                d=serializer2.data
                d['image1']=str+serializer2.data['image1']
                d['image2']=str+serializer2.data['image2']
                d['image3']=str+serializer2.data['image3']
                ather_name=travellouge.auther.username
                d['ather_username']=ather_name
                d['places_titles']=[]
                for p in d['places']:
                    __place=Places.objects.get(id=p)
                    d['places_titles'].append({'id':p,'title':__place.title})
                data['travellouges'].append(d)
            return Response(data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

class SpecificTravellougeAPI(APIView):
    permission_classes=(AllowAny,)
    serializer_class=SpecificSerializer
    serializer_class2=TravellougeSerializer

    def post(self, request, format=None):
        serializer=self.serializer_class(request.data)

        travellouge=TravelLouge.objects.get(id=serializer.data['objID'])
        serializer2=self.serializer_class2(travellouge)
        d=serializer2.data
        ather_name=travellouge.auther.username
        d['image1']=str+serializer2.data['image1']
        d['image2']=str+serializer2.data['image2']
        d['image3']=str+serializer2.data['image3']
        d['ather_username']=ather_name
        d['places_titles']=[]
        for p in d['places']:
            __place=Places.objects.get(id=p)
            d['places_titles'].append({'id':p,'title':__place.title})

        return Response(d,status=status.HTTP_200_OK)