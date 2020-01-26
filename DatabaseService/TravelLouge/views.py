from django.shortcuts import render
from Places.models import Places
from Users.models import user,Leader
from Users.serializers import UserSerializer,LeaderSerializer,PlaceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from DatabaseService.Global_variables import DatabaseServiceURL
from django.core.files.uploadedfile import InMemoryUploadedFile
from .models import TravelLouge
from Places.models import Places
# Create your views here.
class AddTravellouge(APIView):
    def post(self,request):
        
        title=request.data['title']
        Description=request.data['description']
        userID=request.user.id
        auther=user.objects.get(id=userID)
        places=request.data['places']
        l=Places.objects.all()
        travellouge=TravelLouge(title=title,description=Description,auther=auther)

        # if('image1' in request.data):
        #     name=request.data['name1']
        #     contentType=request.data['content_type1']
        #     image1=request.data[name]
        #     image1.content_type=contentType
        
        # if('image2' in request.data):
        #     name=request.data['name2']
        #     contentType=request.data['content_type2']
        #     image2=request.data[name]
        #     image2.content_type=contentType
        
        # if('image3' in request.data):
        #     name=request.data['name3']
        #     contentType=request.data['content_type3']
        #     image3=request.data[name]
        #     image3.content_type=contentType
        
        # travellouge.image1=image1
        # travellouge.image2=image2
        # travellouge.image3=image3

        travellouge.save()
        for pID in places:
            place=Places.objects.get(id=pID)
            travellouge.places.add(place)
        content = {'detail': 'Travellouge Added Successfully Into DataBase!!'}
        return Response(content,status=status.HTTP_201_CREATED)
