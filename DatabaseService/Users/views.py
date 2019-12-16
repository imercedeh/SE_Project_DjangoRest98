from django.shortcuts import render
from .models import user,Leader
from .serializers import UserSerializer,LeaderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from DatabaseService.Global_variables import DatabaseServiceURL

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
    def post(self,request,format=None,*args, **kwargs):
        print(request.data)
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
        print(request.data)
        if('avatar' in request.data):
            u.avatar=request.data['avatar']
        u.save()
        content = {'detail': 'Successfully added user'}
        return Response(content,status=status.HTTP_201_CREATED)
 

        

