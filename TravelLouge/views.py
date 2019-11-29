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

# Create your views here.
str="http://127.0.0.1:8000"
class TravelLougeCreationAPI(APIView):
    permission_classes=(IsAuthenticated,)
    serializer_class =TravelLougeCreationSerializer
        
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            auther=user.objects.get(username=request.user)
            title = serializer.data['title']
            description = serializer.data['description']
            places=serializer.data['places']
            try:
                travellouge=TravelLouge(auther=auther,title=title,description=description)
                
                if('image1' in request.data):
                    travellouge.image1=request.data['image1']
                if('image2' in request.data):
                    travellouge.image2=request.data['image2']
                if('image3' in request.data):
                    travellouge.image3=request.data['image3']
                
                travellouge.save()
        
                for p in places:
                    place=Places.objects.get(id=p)
                    travellouge.places.add(place)

                content = {
                    'detail':'successfuly added the travellouge'}

                return Response(content, status=status.HTTP_201_CREATED)
            except:
                content = {'detail': 'Failed to add travellouge'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
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