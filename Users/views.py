from django.shortcuts import render
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import SignupSerializer
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