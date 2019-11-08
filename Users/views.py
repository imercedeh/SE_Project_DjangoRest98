from django.shortcuts import render
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer,LeaderCreationSerializer,LeaderSerializer
from rest_framework import status

class SignupAPI(CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = user.objects.all()
    serializer_class=UserSerializer

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
