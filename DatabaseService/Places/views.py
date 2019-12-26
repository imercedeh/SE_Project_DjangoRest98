from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Places
from  Users.models import user,Leader
from .serializers import CreatePlaceSerializer,ViewPlaceSerializer,SpecificSerializer
from Users.serializers import UserSerializer
# import logging
# # Create your views here.
# logger = logging.getLogger(__name__)
class AddPlace(APIView):
    def post(self,request):
        # ll=request.data['title']
        # print(ll)
        # response = request.data#.get(url)
        # logger.info(type(response))
        title=request.data['title']
        # image1=request.data['image1']
        # image2=request.data['image2']
        # image3=request.data['image3']
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

        #     places.image1=image1

            
  
        places.save()
        content = {'detail': 'Place Added Successfully Into DataBase!!'}
        return Response(content,status=status.HTTP_201_CREATED)
        # except:
        #     content = {'detail': 'Failed To Add A Place Into DataBase!!'}
        #     return Response(content,status=status.HTTP_201_CREATED)

class GetUniquePlace(APIView):

    def post(self,request,format=None,*args, **kwargs):
        #objectid=request.objID
        objid=request.data['objID']
        place=Places.objects.get(id=objid)#id=serializer.data['objID'])
        #leader=Leader.objects.get(id=place.id)
        #leader=Places.objects.get(place.leader)
        dataa=place.leader.all()
        #leaders={}
        specificdatas={}
        specificdatas['leaders']=[]
        dic={}
        files={}
        print("hi")
        print(dataa)
        for i in dataa:
            u=user.objects.get(username=i.userID)
            serializer3=UserSerializer(u)
            #d=serializer3.data
            #print(type(d))
            #specificdatas['leader']=serializer3.L
            print(i)
            dic['id']=serializer3.data['id']

            if('avatar' in request.FILES):
                dic['avatar']=request.FILES['avatar']
            
            dic['username']=serializer3.data['username']
            print(dic)
            specificdatas['leaders'].append(dict(dic))
            # specificdatas.update()

        print("--------------------")
        print(specificdatas)

        serializer2=ViewPlaceSerializer(place)
        #serializer3=self.serializer_class3(u)

        # specificdatas={}
        # d=serializer3.data
        # #print(type(d))
        # specificdatas['avatar']=url+serializer3.data['avatar']
        # specificdatas['username']=serializer3.data['username']
        # specificdatas.(d['avatar'])
        # specificdatas.append(d['username'])
        data=serializer2.data
        data.update(specificdatas)

        # content = {'detail':('Retrive desired Data form db:')}
        #response=request.post(data=data,files=files)
        return Response(data=data)#,status=status.HTTP_200_OK)
        #return Response(data=data,files=files)
        # try:
        #     title=request.data['title']
        #     place=Places.objects.get(title=title) 
        #     # data=CreatePlaceSerializer(place).data
        #     return Response(data=data,status=status.HTTP_200_OK)
        # except :
        #     content = {'detail':
        #                 ('place does not exist in database.')}
        #     return Response(content, status=status.HTTP_400_BAD_REQUEST)


