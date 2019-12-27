from django.db.models import Q
from rest_framework.generics import CreateAPIView
from Places.models import Places,Comment
from .serializers import CreatePlaceSerializer,ViewPlaceSerializer,HomePlaces,SpecificSerializer,CommentSerializer
from rest_framework import generics
from django.http import Http404
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .filters import *
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.views import APIView
from Users.serializers import UserSerializer,LeaderSerializer,RateSerializer
from Users.models import user,Leader,LeaderRate
import random 

url="http://127.0.0.1:8000"

class CreatePlaceAPIView(APIView):
    queryset = Places.objects.all()
    serializer_class=CreatePlaceSerializer
    #permission_classes = (IsAuthenticated,)

    def post(self,request,format=None):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            title=serializer.data['title']
            image1=serializer.data['image1']
            image2=serializer.data['image2']
            image3=serializer.data['image3']
            Description=serializer.data['Description']
            Likes=serializer.data['Likes']
            categories=serializer.data['categories']
            Hardness=serializer.data['Hardness']
            Address=serializer.data['Address']
            Time=serializer.data['Time']
            StartTime=serializer.data['StartTime']
            EndTime=serializer.data['EndTime']
            City=serializer.data['City']
            try:
                places=Places(title=title,image1=image1,image2=image2,image3=image3,Description=Description,
                    Likes=Likes,categories=categories,Hardness=Hardness,Address=Address,Time=Time,StartTime=StartTime,
                    EndTime=EndTime,City=City)
                places.save()
                content = {'detail': 'Place Added Successfully!!'}
                return Response(content,status=status.HTTP_201_CREATED)
            except:
                content = {'detail': 'Failed To Add A Place!!'}
                return Response(content,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)





class ViewPlaceAPI(generics.ListAPIView):
    serializer_class=ViewPlaceSerializer
    #filter_class = PlacesFilter
    filter_backends= [SearchFilter, OrderingFilter]
    search_fields =  ['id','title', 'Likes','categories','Hardness','Time','StartTime','EndTime','City']

    def get_queryset(self,*args,**kwargs):
        queryset_list = Places.objects.all()
        query=self.request.GET.get('q')
        if query is not None:
            queryset_list=queryset_list.filter(
                Q(id__iexact=query)|
                Q(title__iexact=query)|
                Q(Likes__iexact=query)|
                Q(categories__iexact=query)|
                Q(Hardness__iexact=query)|
                Q(Time__iexact=query)|
                Q(StartTime__iexact=query)|
                Q(EndTime__iexact=query)|
                Q(City__iexact=query)
            ).distinct()
        return queryset_list

class SearchView(generics.ListAPIView):
    filter_backends = (DynamicSearchFilter,)
    queryset = Places.objects.all()
    serializer_class = ViewPlaceSerializer


class UniquePlaceAPI(APIView):
    queryset=Places.objects.all()
    serializer_class=SpecificSerializer
    serializer_class2=ViewPlaceSerializer
    serializer_class3=UserSerializer
    serializer_class4=RateSerializer

    def post(self,request,format=None):
        serializer=self.serializer_class(request.data)
        print(serializer)

        place=Places.objects.get(id=serializer.data['objID'])
        dataa=place.leader.all()
        specificdatas={}
        specificdatas['leaders']=[]
        dic={}
        print("dataaaaaa")
        print(dataa)

        for i in dataa:
            u=user.objects.get(username=i.userID)
            serializer3=self.serializer_class3(u)
            # ratedata=LeaderRate.objects.get(leader=i)
            # serializer4=self.serializer_class4(ratedata)
            # print("--------------ratdata")
            # print(ratedata)
            # print("------------serializer4")
            # print(serializer4)
            # print(i)
            dic['is_available']=i.is_available
            dic['id']=serializer3.data['id']
            dic['avatar']=serializer3.data['avatar']
            dic['username']=serializer3.data['username']
            print(dic)
            specificdatas['leaders'].append(dict(dic))

        serializer2=self.serializer_class2(place)
        data=serializer2.data
        data.update(specificdatas)
        return Response(data,status=status.HTTP_200_OK)




class RandomPlaces(APIView):
    serializer_class = HomePlaces

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
            serializer1=self.serializer_class(placeid)

            dic['id']=serializer1.data['id']
            dic['title']=serializer1.data['title']
            dic['image1']=serializer1.data['image1']
            dic['categories']=serializer1.data['categories']

            specificdata['Home Place'].append(dict(dic))
        return Response(specificdata,status=status.HTTP_200_OK)



class PlaceAdvanceSearch(viewsets.ModelViewSet):
    __basic_fields = ('id','title', 'Likes','categories','Hardness','Time','StartTime','EndTime','City')
    queryset = Places.objects.all()
    serializer_class = ViewPlaceSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields


class PostComment(APIView):
    serializer_class=CommentSerializer

    def post(self,request,format=None):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            comment=serializer.data['comment']
            owner=user.objects.get(id=serializer.data['user'])
            place=Places.objects.get(id=serializer.data['place'])

            try:
                comments=Comment(comment=comment,user=owner,place=place)
                comments.save()
                content = {'detail': 'Comment Added Successfully!!'}
                return Response(content,status=status.HTTP_201_CREATED)
            except:
                content = {'detail': 'Failed To Add A Comment!!'}
                return Response(content,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


class GetComment(APIView):
    serializer_class2=CommentSerializer
    serializer_class=SpecificSerializer
    serializer_class3=UserSerializer
    serializer_class4=ViewPlaceSerializer

    def post(self,request,format=None):
        serializer=self.serializer_class(data=request.data)

        if serializer.is_valid():
            comment=Comment.objects.get(id=serializer.data['objID'])

            specificdatas={}
            specificdatas['Comment']=[]
            dic={}
            serilizer2=self.serializer_class2(comment)
            dataa=Places.objects.get(id=serilizer2.data['place'])
            serializer4=self.serializer_class4(dataa)
            owner=user.objects.get(id=serilizer2.data['user'])
            serializer3=self.serializer_class3(owner)   
            dic['Owner']=serializer3.data['username']
            dic['id']=serializer3.data['id']
            print(owner)
            specificdatas['Comment'].append(dict(dic))

        data=serializer4.data
        data.update(specificdatas)
        return Response(data,status=status.HTTP_200_OK)
