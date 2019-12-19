from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Places
from .serializers import CreatePlaceSerializer
# import logging
# # Create your views here.
# logger = logging.getLogger(__name__)
class AddPlace(APIView):
    def post(self,request):
        # ll=request.data['title']
        # print(ll)
        # response = request.data#.get(url)
        # logger.info(type(response))
        title=request.data['title']
        # image1=request.data['image1']
        # image2=request.data['image2']
        # image3=request.data['image3']
        Description=request.data['Description']
        Likes=request.data['Likes']
        categories=request.data['categories']
        Hardness=request.data['Hardness']
        Address=request.data['Address']
        Time=request.data['Time']
        StartTime=request.data['StartTime']
        EndTime=request.data['EndTime']
        City=request.data['City']
        # try:
        places=Places(title=title,Description=Description,
                    Likes=Likes,categories=categories,Hardness=Hardness,Address=Address,Time=Time,StartTime=StartTime,
                    EndTime=EndTime,City=City)


        if('image1' in request.FILES):
            places.image1=request.FILES['image1']

        if('image2' in request.FILES):
            places.image2=request.FILES['image2']


        if('image3' in request.FILES):
            places.image3=request.FILES['image3']

        #     places.image1=image1

            
  
        places.save()
        content = {'detail': 'Place Added Successfully Into DataBase!!'}
        return Response(content,status=status.HTTP_201_CREATED)
        # except:
        #     content = {'detail': 'Failed To Add A Place Into DataBase!!'}
        #     return Response(content,status=status.HTTP_201_CREATED)

class GetPlace(APIView):
    def get(self,request,format=None,*args, **kwargs):
        try:
            title=request.data['title']
            place=Places.objects.get(title=title) 
            # data=CreatePlaceSerializer(place).data
            return Response(data=data,status=status.HTTP_200_OK)
        except :
            content = {'detail':
                        ('place does not exist in database.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


