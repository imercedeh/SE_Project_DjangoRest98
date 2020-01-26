from django.shortcuts import render
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
import requests
from rest_framework.views import APIView
from GateWay.Global_variables import UserServiceURL,PlaceServiceURL,TravellougeServiceURL
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
    #permission_classes = (IsAuthenticated,)
    def post(self, request):
        url=UserServiceURL+"leadercreation/"
        data=request.data
        headers=dict(request.headers)
        header={}
        header['Authorization']=headers['Authorization']
        resualt=requests.post(url=url,headers=header,data=data)
        return Response(data=resualt.json())


class LeadPlace(APIView):
    #permission_classes = (IsAuthenticated,)
    def post(self, request):
        url=UserServiceURL+"LeadPlace/"
        data=request.data
        headers=dict(request.headers)
        header={}
        header['Authorization']=headers['Authorization']
        resualt=requests.post(url=url,headers=header,data=data)
        return Response(data=resualt.json())


class ChangeAvailability(APIView):
    #permission_classes=(IsAuthenticated,)

    def post(self, request, format=None):
        url=UserServiceURL+"ChangeAvailability/"
        headers=request.headers
        response=requests.post(url=url,headers=headers)
        return Response(response.json())

class TravelLougeCreation(APIView):
    #permission_classes=(IsAuthenticated,)
    def post(self, request,format=None):
        url=TravellougeServiceURL+"travellouge-creation/"
        data=request.data
        data = json.dumps(data)
        headers=dict(request.headers)
        files={}
        # if('image1' in data):
        #     pic1=data['image1']
        #     files={pic1.name:pic1.file}
        #     data['image1']='True'
        #     data['content_type1']=pic1.content_type
        #     data['name1']=pic1.name
       
        # if('image2' in data):
        #     pic2=data['image2']
        #     files={pic2.name:pic2.file}
        #     data['image2']='True'
        #     data['content_type2']=pic2.content_type
        #     data['name2']=pic2.name
        
        # if('image3' in data):
        #     pic3=data['image3']
        #     files={pic3.name:pic3.file}
        #     data['image3']='True'
        #     data['content_type3']=pic3.content_type
        #     data['name3']=pic3.name    
            

        response=requests.post(url=url,data=data,files=files,headers=headers)
        return Response(response.json())


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
