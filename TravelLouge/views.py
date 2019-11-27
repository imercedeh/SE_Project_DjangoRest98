from django.shortcuts import render
from .models import TravelLouge
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import TravelLougeCreationSerializer
from rest_framework import status
from Places.models import Places
from Users.models import user,Leader

# Create your views here.
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