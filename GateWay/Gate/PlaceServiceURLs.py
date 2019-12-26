from django.conf.urls import url
from django.contrib import admin
from Gate.views import CreatePlace,UniquePlace#,ViewPlace,RandomPlaces,PlaceAdvanceSearch,SearchView

urlpatterns = [
    url(r'CreatePlace/', CreatePlace.as_view(), name='create'), 
    #url(r'ViewPlace/', ViewPlace.as_view(), name='View'), 
    url(r'UniquePlace/',UniquePlace.as_view(),name='unique'),  
    # url(r'RandomPlace/',RandomPlaces.as_view(),name='random'),
    # url(r'PlaceAdvanceSearch/',PlaceAdvanceSearch.as_view({'get': 'list'}),name='PlaceAdvanceSearch'), 
    # url(r'SearchView/',SearchView.as_view(),name='serachview'),
]