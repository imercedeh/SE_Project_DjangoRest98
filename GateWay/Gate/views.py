from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
import requests
from rest_framework.views import APIView
from GateWay.Global_variables import UserServiceURL,PlaceServiceURL
import json

class Signup(APIView):
    permission_classes = (AllowAny,)
    def post(self, request,format=None):
        url=UserServiceURL+"sign-up/"
        data=request.data
        files={}

        if('avatar' in data):
            pic=data['avatar']
            files={pic.name:pic.file}
            data['avatar']='True'
            data['content_type']=pic.content_type
            data['name']=pic.name
            
        response=requests.post(url=url,data=data,files=files)
        return Response(data=response.json())

class Login(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        url=UserServiceURL+"token/"
        data=request.data
        resualt=requests.post(url=url,data=data)
        return Response(data=resualt.json())


class LeaderCreation(APIView):
    permission_classes=(IsAuthenticated,)
    def post(self, request):
        url=UserServiceURL+"leadercreation/"
        data=request.data
        resualt=requests.post(url=url,data=data)
        return Response(data=resualt.json())

class CreatePlace(APIView):
    def post(self, request,format=None):
        url=PlaceServiceURL+"CreatePlace/"
        data=request.data
        files={}
         
        if('image1' in request.data):
            files={'image1':request.data['image1']}
            print(data)


        if('image2' in request.data):
            files={'image2':request.data['image2']}
            print(data)



        if('image3' in request.data):
            files={'image3':request.data['image3']}
            print(data)

        response=requests.post(url=url,data=data,files=files)
        return Response(data=response.json())


class UniquePlace(APIView):
    def post(self,request,format=None):
        url=str(PlaceServiceURL)+'UniquePlace/'
        data=request.data
        print(data)
        files={}

        if('image1' in request.data):
            files={'image1':request.data['image1']}

        if('image2' in request.data):
            files={'image2':request.data['image2']}


        if('image3' in request.data):
            files={'image3':request.data['image3']}


        if('avatar' in request.data):
            files={'avatar':request.data['avatar']}
        
        response=requests.post(url=url,data=data,files=files)
        return Response(data=response.json(encoding=ascii))


class RandomPlace(APIView):
    def post(self,request,format=None):
        url=str(PlaceServiceURL)+'RandomPlace/'
        data=request.data
        print(data)
        files={}

        if('image1' in request.data):
            files={'image1':request.data['image1']}
        
        response=requests.post(url=url,data=data,files=files)
        return Response(data=response.json(encoding=ascii))
