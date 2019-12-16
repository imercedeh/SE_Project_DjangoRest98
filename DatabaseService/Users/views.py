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
            return Response(data=data)
        except :
            content = {'detail':
                        ('username does not exist in db.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

        

