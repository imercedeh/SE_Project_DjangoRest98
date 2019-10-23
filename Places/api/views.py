from django.db.models import Q
from rest_framework.generics import CreateAPIView
from .serializers import CreatePlaceSerializer
from Places.models import *


class CreatePlaceAPIView(CreateAPIView):
    queryset = Places.objects.all()
    serializer_class = CreatePlaceSerializer

    def perform_create(self, serializer):
        serializer.save() 