from django.shortcuts import render
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import SignupSerializer,UserSerializer,LeaderCreationSerializer,LeaderSerializer
from rest_framework import status
from rest_framework.filters import SearchFilter

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

    def get(self, request, format=None):
        u=user.objects.get(username=request.user.username)
        serializer1=self.serializer_class1(u)
        if(u.is_leader):
            leader=Leader.objects.get(userID=request.user)
            serializer2=self.serializer_class2(leader)
            content=dict(serializer1.data)
            content.update(dict(serializer2.data))
            return Response(content,status=status.HTTP_200_OK)
        else:
            return Response(serializer1.data,status=status.HTTP_200_OK)   


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

class SpecificLeaderAPI(generics.ListAPIView):
    queryset=Leader.objects.all()
    serializer_class=LeaderSerializer
    filter_backends= [SearchFilter]
    search_fields = ['id']
    
    def get_queryset(self):
        queryset = Leader.objects.all()
        id = self.request.query_params.get('search')
        if id is not None:
             queryset = queryset.filter(id__exact=id).distinct()
        return queryset

class SpecificUserAPI(generics.ListAPIView):
    queryset=user.objects.all()
    serializer_class=UserSerializer
    filter_backends= [SearchFilter]
    search_fields = ['id']
    
    def get_queryset(self):
        queryset =user.objects.all()
        id = self.request.query_params.get('search')
        if id is not None:
             queryset = queryset.filter(id__exact=id).distinct()
        return queryset
