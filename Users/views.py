from django.shortcuts import render
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignupSerializer,UserSerializer,LeaderCreationSerializer,LeaderSerializer
from rest_framework import status

class SignupAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            username = serializer.data['username']
            email = serializer.data['email']
            password = serializer.data['password']
            first_name = serializer.data['first_name']
            last_name = serializer.data['last_name']
            itinerary=serializer.data['itinerary']
            phone_number=serializer.data['phone_number']

            try:
                u = user.objects.get(username=username)
                content = {'detail':
                        ('User with this Username already exists.')}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
            except:
                u=user.objects.create_user(username=username,email=email,password=password,
                    first_name=first_name,last_name=last_name)
                u.itinerary=itinerary
                u.phone_number=phone_number
                u.save()

                content = {'username': username ,'email': email, 'first_name': first_name,
                    'last_name': last_name,'itinerary':itinerary,'phone_number':phone_number }

                return Response(content, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)
from .serializers import UserSerializer
from rest_framework import status

class UserAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, format=None):
        u=user.objects.get(username=request.user.username)
        serializer=self.serializer_class(u)
        return Response(serializer.data,status=status.HTTP_200_OK)

class LeaderCreationAPI(APIView):
    permission_classes=(IsAuthenticated,)
    serializer_class =LeaderCreationSerializer
        
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        u=user.objects.get(username= request.user.username)
        if(u.is_leader):
            content = {'detail': 'Leader with tihs information already exits!'}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            nationalID = serializer.data['nationalID']
            has_car = serializer.data['has_car']
            car_capacity = serializer.data['car_capacity']
            car_model = serializer.data['car_model']

            try:
                u.is_leader=True
                u.save()
                leader=Leader(userID=u,nationalID=nationalID,has_car=has_car,
                car_capacity=car_capacity,car_model=car_model)
                leader.save()
                content = {'username': leader.userID.username ,'nationalID':leader.nationalID,
                    'detail':'successfuly added the leader'}

                return Response(content, status=status.HTTP_201_CREATED)
            except:
                content = {'detail': 'Failed to add leader'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
             return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

class LeaderAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LeaderSerializer

    def get(self, request, format=None):
        leader=Leader.objects.get(userID=request.user)
        serializer=self.serializer_class(leader)
        u=user.objects.get(username=request.user)
        content = {'username': u.username ,'email': u.email, 'first_name': u.first_name,
                    'last_name': u.last_name,'itinerary':u.itinerary,'phone_number':u.phone_number }
        content.update(dict(serializer.data))
        return Response(content,status=status.HTTP_200_OK)
