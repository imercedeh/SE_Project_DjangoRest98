from django.conf.urls import url
from django.contrib import admin

from .views import CreatePlaceAPIView,ViewPlaceAPI,UniquePlaceAPI,RandomPlaces,SearchView

urlpatterns = [
    url(r'CreatePlace/', CreatePlaceAPIView.as_view(), name='create'), 
    url(r'ViewPlace/', ViewPlaceAPI.as_view(), name='View'), 
    url(r'UniquePlace/',UniquePlaceAPI.as_view(),name='unique'),  
    url(r'RandomPlace/',RandomPlaces.as_view(),name='random'),
    url(r'SearchView/',SearchView.as_view(),name='serachview'),
]