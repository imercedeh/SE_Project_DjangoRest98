from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Places
from  Users.models import user,Leader
from .serializers import CreatePlaceSerializer,ViewPlaceSerializer,SpecificSerializer,HomePlaces
from Users.serializers import UserSerializer
from Users.serializers import PlaceSerializer
import random

class GetPlace(APIView):
    def get(self,request):
        try:
            id=request.data['objID']
            place=Places.objects.get(id=id) 
            data=PlaceSerializer(place).data
            return Response(data=data,status=status.HTTP_200_OK)
        except :
            content = {'detail':
                        ('place does not exist in db.')}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)

class AddPlace(APIView):
    def post(self,request):
        title=request.data['title']
        Description=request.data['Description']
        Likes=request.data['Likes']
        categories=request.data['categories']
        Hardness=request.data['Hardness']
        Address=request.data['Address']
        Time=request.data['Time']
        StartTime=request.data['StartTime']
        EndTime=request.data['EndTime']
        City=request.data['City']
        # try:
        places=Places(title=title,Description=Description,
                    Likes=Likes,categories=categories,Hardness=Hardness,Address=Address,Time=Time,StartTime=StartTime,
                    EndTime=EndTime,City=City)


        if('image1' in request.FILES):
            places.image1=request.FILES['image1']

        if('image2' in request.FILES):
            places.image2=request.FILES['image2']


        if('image3' in request.FILES):
            places.image3=request.FILES['image3']
  
        places.save()
        content = {'detail': 'Place Added Successfully Into DataBase!!'}
        return Response(content,status=status.HTTP_201_CREATED)

class GetUniquePlace(APIView):

    def post(self,request,format=None,*args, **kwargs):
        objid=request.data['objID']
        place=Places.objects.get(id=objid)
        dataa=place.leader.all()
        specificdatas={}
        specificdatas['leaders']=[]
        dic={}
        files={}
        print("hi")
        print(dataa)
        for i in dataa:
            u=user.objects.get(username=i.userID)
            serializer3=UserSerializer(u)
            print(i)
            dic['id']=serializer3.data['id']

            if('avatar' in request.FILES):
                dic['avatar']=request.FILES['avatar']
            
            dic['username']=serializer3.data['username']
            print(dic)
            specificdatas['leaders'].append(dict(dic))

        print("--------------------")
        print(specificdatas)

        serializer2=ViewPlaceSerializer(place)
        data=serializer2.data
        data.update(specificdatas)

        return Response(data=data)


class GetRandomPlace(APIView):
    def get(self,request):
        data=Places.objects.all()
        dic={}
        specificdata={}
        specificdata['Home Place']=[]
        uniquenumbers=[]

        while(len(uniquenumbers) < 3 ):
            number=random.randint(1,len(data))
            print(number)
            if number not in uniquenumbers:
                uniquenumbers.append(number)
        for k in uniquenumbers:
            placeid=data.get(id=k)
            serializer1=HomePlaces(placeid)

            dic['id']=serializer1.data['id']
            dic['title']=serializer1.data['title']
            dic['image1']=serializer1.data['image1']
            dic['categories']=serializer1.data['categories']

            specificdata['Home Place'].append(dict(dic))
        return Response(specificdata,status=status.HTTP_200_OK)