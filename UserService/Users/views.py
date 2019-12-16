from django.shortcuts import render
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import SignupSerializer,UserSerializer,LeaderCreationSerializer,LeaderSerializer,PlaceSerializer
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer,LeaderCreationSerializer,LeaderSerializer,LeadPlaceSerializer,SpecificSerializer
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.parsers import MultiPartParser, FormParser,FileUploadParser
from Places.models import Places
from TravelLouge.models import TravelLouge
from TravelLouge.serializers import TravellougeSerializer
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
import json
from django.db.models import Q
from .Global_variables import URL

class SignupAPI(APIView):
    serializer_class = SignupSerializer
    def post(self, request):
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
                if('avatar' in request.data):
                    u.avatar=request.data['avatar']
                u.save()
                content = {'detail': 'Successfully added user'}
                return Response(content,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

class ProfileAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class1 = UserSerializer
    serializer_class2 = LeaderSerializer
    serializer_class3=PlaceSerializer
    serializer_class4=TravellougeSerializer

    def get(self, request, format=None):
        u=user.objects.get(username=request.user.username)
        serializer1=self.serializer_class1(u)
        data=serializer1.data
        data['avatar']=URL+serializer1.data['avatar']

        travellouges=TravelLouge.objects.filter(auther=u.id)
        data['travellouges']=[]

        for travellouge in travellouges:
            serializer4=self.serializer_class4(travellouge)
            d=serializer4.data
            d['image1']=URL+serializer4.data['image1']
            d['image2']=URL+serializer4.data['image2']
            d['image3']=URL+serializer4.data['image3']
            data['travellouges'].append(d)
        
        if(u.is_leader):
            leader=Leader.objects.get(userID=request.user)
            serializer2=self.serializer_class2(leader)
            set=list(leader.places_set.all())
            data['place']=[]

            for place in set:
                serializer3=self.serializer_class3(place)
                data['place'].append(serializer3.data)
            data.update(dict(serializer2.data))

        return Response(data,status=status.HTTP_200_OK)
   


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
            gender=serializer.data['gender']
            age=serializer.data['age']

            try:
                u.is_leader=True
                u.save()
                leader=Leader(userID=u,nationalID=nationalID,has_car=has_car,
                car_capacity=car_capacity,car_model=car_model,gender=gender,age=age)
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

class SpecificLeaderAPI(APIView):
    permission_classes=(IsAuthenticated,)
    serializer_class=SpecificSerializer
    serializer_class2=LeaderSerializer
    serializer_class3=UserSerializer

    def post(self, request, format=None):
        serializer=self.serializer_class(request.data)

        leader=Leader.objects.get(id=serializer.data['objID'])
        u=user.objects.get(username=leader.userID)

        serializer2=self.serializer_class2(leader)
        serializer3=self.serializer_class3(u)
        
        d=serializer3.data
        d['avatar']=URL+serializer3.data['avatar']
        data=serializer2.data
        data.update(d)
        return Response(data,status=status.HTTP_200_OK)



class SpecificUserAPI(generics.ListAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class=SpecificSerializer
    serializer_class2=UserSerializer

    def post(self, request, format=None):
        serializer=self.serializer_class(request.data)

        u=user.objects.get(id=serializer.data['objID'])
        serializer2=self.serializer_class2(u)
        
        data=serializer2.data
        data['avatar']=URL+serializer2.data['avatar']
        return Response(data,status=status.HTTP_200_OK)

class LeadPlaceAPI(APIView):
    permission_classes=(IsAuthenticated,)
    serializer_class =LeadPlaceSerializer
        
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                leader=Leader.objects.get(userID=request.user)
                place=Places.objects.get(pk=serializer.data['placeID'])
                place.leader.add(leader)
                content = {'detail': 'Added place successfuly'}
                return Response(content, status=status.HTTP_200_OK)
            except:
                content = {'detail': 'Failed to add place'}
                return Response(content, status=status.HTTP_400_BAD_REQUEST)
        else:
             return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

class ChangeAvailabilityAPI(APIView):
    permission_classes=(IsAuthenticated,)

    def post(self, request, format=None):
        u=user.objects.get(username=request.user.username)
        leader=Leader.objects.get(userID=u)
        leader.is_available=not leader.is_available
        leader.save()
        return Response(status=status.HTTP_200_OK)


class LeadersView(APIView):
    def get(self,request,format=None,*args, **kwargs):
        leader=user.objects.all()
        serializer=LeaderSerializer(leader,many=True)
        return Response({"List Of All Leaders ":serializer.data})


class LeaderAdvanceSearch(viewsets.ModelViewSet):
    __basic_fields = ('id','nationalID','car_model','age','userID')
    queryset = Leader.objects.all()
    serializer_class = LeaderSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields


class LeaderSortView(generics.ListAPIView):
    queryset=Leader.objects.all()
    serializer_class=LeaderSerializer
    filter_backends= [OrderingFilter]
    search_fields = ['id','nationalID','car_model','age','userID']
class UsersView(APIView):
    def get(self,request,format=None,*args, **kwargs):
        users=user.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response({"List Of All users ":serializer.data})

class UserAdvanceSearch(viewsets.ModelViewSet):
    __basic_fields = ('id','username', 'email', 'first_name', 'last_name')
    queryset = user.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields

