from django.conf.urls import url
from django.contrib import admin

from .views import CreatePlaceAPIView

urlpatterns = [
    url(r'CreatePlace/', CreatePlaceAPIView.as_view(), name='create'),   
]