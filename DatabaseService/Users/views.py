from django.shortcuts import render
from .models import user,Leader
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import requests




class Signup(APIView):

    def post(self, request):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        itinerary=request.data['itinerary']
        phone_number=request.data['phone_number']
        try:
            u = user.objects.get(username=username)
            content = {'detail':
                        ('User with this Username already exists.')}
            content=serializer.data
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
        

