from django.shortcuts import render
from .models import user,Leader
from .serializers import UserSerializer,LeaderSerializer,PlaceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from DatabaseService.Global_variables import DatabaseServiceURL
from django.core.files.uploadedfile import InMemoryUploadedFile
from Places.models import Places

class GetUser(APIView):
    def get(self,request,format=None,*args, **kwargs):
        try:
            username=request.data['username']
            singleuser=user.objects.get(username=username) 
            data=UserSerializer(singleuser).data
            data['avatar']=DatabaseServiceURL+data['avatar']
            return Response(data=data,status=status.HTTP_200_OK)
        except :
            content = {'detail':
                        ('username does not exist in db.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class AddUser(APIView):
    def post(self,request):

        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        itinerary=request.data['itinerary']
        phone_number=request.data['phone_number']

        u=user.objects.create_user(username=username,email=email,password=password,
                    first_name=first_name,last_name=last_name)
        u.itinerary=itinerary
        u.phone_number=phone_number

        if('avatar' in request.data):
            name=request.data['name']
            contentType=request.data['content_type']
            avatar=request.data[name]
            avatar.content_type=contentType

            u.avatar=avatar
        u.save()
        content = {'detail': 'Successfully added user'}
        return Response(content,status=status.HTTP_201_CREATED)

class GetLeader(APIView):
    def get(self,request):
        try:
            userID=request.user.id
            u=user.objects.get(id=userID)
            leader=Leader.objects.get(userID=userID)
            data=UserSerializer(u).data 
            leaderData=LeaderSerializer(leader).data
            data.update(dict(leaderData))
            data['avatar']=DatabaseServiceURL+data['avatar']
            return Response(data=data,status=status.HTTP_200_OK)
        except :
            content = {'detail':
                        ('leader does not exist in db.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class AddLeader(APIView):

    def post(self,request):
        nationalID = request.data['nationalID']
        has_car = request.data['has_car']
        car_capacity = request.data['car_capacity']
        car_model = request.data['car_model']
        gender = request.data['gender']
        age=request.data['age']
        userID=request.user.id

        u=user.objects.get(id=userID)
        u.is_leader=True
        u.save()

        leader=Leader(userID=u,nationalID=nationalID,has_car=has_car,
                car_capacity=car_capacity,car_model=car_model,gender=gender,age=age)
        leader.save()

        content = {'detail': 'Successfully added Leader'}
        return Response(content,status=status.HTTP_201_CREATED)


class LeadPlace(APIView):

    def post(self,request):
        
        data=request.data
        leaderID=data['leader']
        placeID=data['place']
        leader=Leader.objects.get(id=leaderID)
        place=Places.objects.get(id=placeID)
    
        place.leader.add(leader)

        content = {'detail': 'Successfully added place'}
        return Response(content,status=status.HTTP_200_OK)
 

        

