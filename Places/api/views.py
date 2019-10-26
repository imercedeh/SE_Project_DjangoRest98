from django.db.models import Q
from rest_framework.generics import CreateAPIView
from Places.models import Places
from .serializers import CreatePlaceSerializer,ViewPlaceSerializer,PlaceImageSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404
from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
)

class CreatePlaceAPIView(CreateAPIView):
    queryset = Places.objects.all()
    serializer_class=CreatePlaceSerializer


class ViewPlaceAPI(generics.ListAPIView):
    queryset = Places.objects.all()
    serializer_class=ViewPlaceSerializer
    serializer_class1=PlaceImageSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    search_fields = ['City', 'title']

    # def get_queryset(self, *args, **kwargs):
    #     queryset_list = Places.objects.all() 
        # user = self.request.user

        # if user is not None:
        #     return Places.objects.filter(user=user)
        # else:
        #     return Http404