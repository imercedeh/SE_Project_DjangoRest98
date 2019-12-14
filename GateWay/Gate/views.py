from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
import requests
from rest_framework.views import APIView

UserServiceUrl="http://localhost:8001/api"

class Signup(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        url=UserServiceUrl+"/sign-up/"
        data=request.data
        resualt=requests.post(url=url,data=data)
        return Response(data=resualt.json())

        


        
