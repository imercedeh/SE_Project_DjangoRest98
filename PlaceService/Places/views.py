from django.db.models import Q
from rest_framework.generics import CreateAPIView
from Places.models import Places
from .serializers import CreatePlaceSerializer,ViewPlaceSerializer,HomePlaces,SpecificSerializer
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
from Users.serializers import UserSerializer
from Users.models import user,Leader
from PlaceService.Global_variables import DatabaseServiceURL,PlaceServiceURL
import requests
import sys, json
from django.conf import settings

class CreatePlace(APIView):
    #queryset = Places.objects.all()
    serializer_class=CreatePlaceSerializer
    #permission_classes = (IsAuthenticated,)



    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            
            title=serializer.data['title']
            response=requests.get(url=DatabaseServiceURL+"Place/GetPlace/",data={'title':title})

            if response.status_code==200:
                content={'detail':'place with this title already exists!'}
                return Response(data=content,status=status.HTTP_400_BAD_REQUEST)

            else:
                files={}
                data=serializer.data

                if('image1' in request.FILES):
                    files={'image1':request.FILES['image1']}

                if('image2' in request.FILES):
                    files={'image2':request.FILES['image2']}

                if('image3' in request.FILES):
                    files={'image3':request.FILES['image3']}

                response=requests.post(url=DatabaseServiceURL+"Place/AddPlace/",data=data,files=files)
                return Response(response.json())
        else:
            return Response(serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

        # if serializer.is_valid():
        #     title=serializer.data['title']
        #     data=serializer.data#json.loads(serializer.data)
        #     print(data)
        #     # json_acceptable_string = datas.replace("'", "\"")
        #     # d = json.loads(json_acceptable_string)
        #     response=requests.post(url=DatabaseServiceURL+'Place/AddPlace/',data=data)
        # return Response(response.json())




class ViewPlaceAPI(generics.ListAPIView):
    serializer_class=ViewPlaceSerializer
    #filter_class = PlacesFilter
    filter_backends= [SearchFilter, OrderingFilter]
    search_fields =  ['id','title', 'Likes','categories','Hardness','Time','StartTime','EndTime','City']

    # def get_queryset(self,*args,**kwargs):
    #     queryset_list = Places.objects.all()
    #     query=self.request.GET.get('q')
    #     if query is not None:
    #         queryset_list=queryset_list.filter(
    #             Q(id__iexact=query)|
    #             Q(title__iexact=query)|
    #             Q(Likes__iexact=query)|
    #             Q(categories__iexact=query)|
    #             Q(Hardness__iexact=query)|
    #             Q(Time__iexact=query)|
    #             Q(StartTime__iexact=query)|
    #             Q(EndTime__iexact=query)|
    #             Q(City__iexact=query)
    #         ).distinct()
    #     return queryset_list

class SearchView(generics.ListAPIView):
    filter_backends = (DynamicSearchFilter,)
    queryset = Places.objects.all()
    serializer_class = ViewPlaceSerializer


class UniquePlace(APIView):
    # queryset=Places.objects.all()
    serializer_class=SpecificSerializer
    # serializer_class2=ViewPlaceSerializer
    # serializer_class3=UserSerializer


    def post(self,request,format=None):
        serializer=self.serializer_class(data=request.data)
        # print(serializer)

        if serializer.is_valid():
            objectid=serializer.data['objID']
            response=requests.post(url=str(DatabaseServiceURL)+'Place/GetUniquePlace/',data={'objID':objectid})
            # print("----------------response-------------------------")
            # print(response)
            # #print(response.json())
            # print("-----------------conetenc------------------------")
            # print(response.content)
            # print("---------------text--------------------------")
            # print(response.text)
            # print("--------------ednc--------------------------")
            # print(response.apparent_encoding)
            # print("---------------dic--------------------------")
            # print(response.__dict__)
            # print("---------------jdon--------------------------")
            # print(response.json(encoding=ascii))
            return Response(response.json(encoding=ascii))
            #data=serializer.data
        # place=Places.objects.get(id=serializer.data['objID'])
        # #leader=Leader.objects.get(id=place.id)
        # #leader=Places.objects.get(place.leader)
        # dataa=place.leader.all()
        # #leaders={}
        # specificdatas={}
        # specificdatas['leaders']=[]
        # dic={}
        # print("hi")
        # print(dataa)
        # for i in dataa:
        #     u=user.objects.get(username=i.userID)
        #     serializer3=self.serializer_class3(u)
        #     #d=serializer3.data
        #     #print(type(d))
        #     #specificdatas['leader']=serializer3.L
        #     print(i)
        #     dic['id']=serializer3.data['id']
        #     dic['avatar']=serializer3.data['avatar']
        #     dic['username']=serializer3.data['username']
        #     print(dic)
        #     specificdatas['leaders'].append(dict(dic))
        #     # specificdatas.update()

        # print("--------------------")
        # print(specificdatas)

        # serializer2=self.serializer_class2(place)
        # #serializer3=self.serializer_class3(u)

        # # specificdatas={}
        # # d=serializer3.data
        # # #print(type(d))
        # # specificdatas['avatar']=url+serializer3.data['avatar']
        # # specificdatas['username']=serializer3.data['username']
        # # specificdatas.(d['avatar'])
        # # specificdatas.append(d['username'])
        # data=serializer2.data
        # data.update(specificdatas)#dict(specificdatas))
        # data.update(leaders)
        # return Response(data,status=status.HTTP_200_OK)

# class UniquePlaceAPI(generics.ListAPIView):

    # queryset=Places.objects.all()
    # serializer_class=ViewPlaceSerializer
    # filter_backends= [SearchFilter]
    # search_fields = ['id']
    
    # def get_queryset(self):
        # queryset = Places.objects.all()
        # id = self.request.query_params.get('search')
        # if id is not None:
             # queryset = queryset.filter(id__exact=id).distinct()
        # return queryset


class RandomPlaces(APIView):
    #queryset = Places.objects.all().order_by('?')[:3]
    serializer_class = HomePlaces
    def get(self,request):
        response=requests.post(url=str(DatabaseServiceURL)+'Place/GetRandomPlace/')
        return Response(response.json(encoding=ascii))


#age ye bar un comment koni hame unaee k dorost kar mikone run mishe
    # def get(self,request):
    #     data=Places.objects.all()
    #     dic={}
    #     specificdata={}
    #     specificdata['Home Place']=[]
    #     uniquenumbers=[]

    #     #for third in range(0,3):
    #     while(len(uniquenumbers) < 3 ):
    #         # uniquecount=len(uniquenumbers)
    #         # print(uniquecount)
    #         # if uniquecount < 4 :#or  uniquecount == 0:
    #         number=random.randint(1,len(data))
    #         print(number)
    #         if number not in uniquenumbers:
    #             uniquenumbers.append(number)
    #             # else:
    #             #     break

    #     print("---------------for balayy----")
    #     print(uniquenumbers)

    #     # for j in range(0,3):
    #     #     print(j)
    #     #     datacount=len(data)
    #     #    # number=random.sample(range(1,datacount),1)
    #     #     number=random.randint(1,datacount)
    #     #     if number not in uniquenumbers and uniquenumbers.count==3:
    #     #         uniquenumbers.append(number)
    #     #     else:
    #     #         return uniquenumbers

    #         # # print("--------------------unique numbers------")
    #         # # print(uniquenumbers)
    #         # if(uniquenumbers.__contains__(number)):

    #         # uniquenumbers.append(number)
    #         # print("------------------number random---------------------------")
    #         # print(number)
    #         #for i in data:
    #     for k in uniquenumbers:
    #                 # print("--------------i------")
    #                 # print(i)
    #                 # print("--------------k------")
    #                 # print(k)
    #         placeid=data.get(id=k)
    #                 # print("----------------place id------------")
    #                 # print(placeid)
    #         serializer1=self.serializer_class(placeid)

    #         dic['id']=serializer1.data['id']
    #         dic['title']=serializer1.data['title']
    #         dic['image1']=serializer1.data['image1']
    #         dic['categories']=serializer1.data['categories']
    #             # print("---------------dic-----")
    #             # print(dic)

    #     # for element in dic:
    #     #     if element not in specificdata:
    #         specificdata['Home Place'].append(dict(dic))

    #     # print("--------specific------------")
    #     # print(specificdata)


    #     return Response(specificdata,status=status.HTTP_200_OK)



class PlaceAdvanceSearch(viewsets.ModelViewSet):
    __basic_fields = ('id','title', 'Likes','categories','Hardness','Time','StartTime','EndTime','City')
    queryset = Places.objects.all()
    serializer_class = ViewPlaceSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields