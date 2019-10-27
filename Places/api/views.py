from django.db.models import Q
from rest_framework.generics import CreateAPIView
from .serializers import CreatePlaceSerializer
from Places.models import Places
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

class CreatePlaceAPIView(CreateAPIView):
    queryset = Places.objects.all()
    serializer_class=CreatePlaceSerializer
    parser_classes = (MultiPartParser, FormParser)


