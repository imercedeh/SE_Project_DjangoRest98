from django.shortcuts import render
from .models import user,Leader,Places,TravelLouge
from rest_framework.views import APIView
from Users.seralizers import UserSerializer,LeaderSerializer
from Places.api.serializers import ViewPlaceSerializer
from TravelLouge.serializers import TravellougeSerializer
from rest_framework.response import Response
# Create your views here.


class LeadersData(APIView):
    def get(self,request,format=None,*args, **kwargs):
        leader=Leader.objects.all()
        serializer=LeaderSerializer(leader,many=True)
        return Response({"Data Of All Leaders ":serializer.data})


class UsersData(APIView):
    def get(self,request,format=None,*args, **kwargs):
        user=user.objects.all()
        serializer=UserSerializer(user,many=True)
        return Response({"Data Of All users ":serializer.data})

class PlacesData(APIView):
    def get(self,request,format=None,*args, **kwargs):
        place=Places.objects.all()
        serializer=ViewPlaceSerializer(place,many=True)
        return Response({"Data Of All Places ":serializer.data})

class TravellougeData(APIView):
    def get(self,request,format=None,*args, **kwargs):
        travellouge=TravelLouge.objects.all()
        serializer=TravellougeSerializer(travellouge,many=True)
        return Response({"Data Of All Travellouge ":serializer.data})

