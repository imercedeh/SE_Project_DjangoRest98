from django.db.models import Q
from rest_framework.generics import CreateAPIView
from .serializers import CreatePlaceSerializer
from Places.models import Places
from .serializers import CreatePlaceSerializer
from rest_framework import status
from rest_framework.response import Response

class CreatePlaceAPIView(CreateAPIView):
    queryset = Places.objects.all()
    serializer_class=CreatePlaceSerializer

    def post(self, request, format=None):
        Place_serializer = self.serializer_class(data=request.data)
        if Place_serializer.is_valid():
            Place_serializer.save()
            return Response(Place_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(Place_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)


