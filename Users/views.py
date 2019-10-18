from django.shortcuts import render
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework import status

class UserAPI(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get(self, request, format=None):
        u=user.objects.get(username=request.user.username)
        serializer=self.serializer_class(u)
        return Response(serializer.data,status=status.HTTP_200_OK)