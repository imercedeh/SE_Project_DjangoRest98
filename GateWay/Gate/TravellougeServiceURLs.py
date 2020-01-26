from django.conf.urls import include, url
from rest_framework.authtoken import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from .views import TravelLougeCreation



urlpatterns = [
    url(r'^travellouge-creation/$', TravelLougeCreation.as_view()),
    #url(r'^place-travellouges/$', PlaceTravelLougesAPI.as_view()),
    #url(r'^SpecificTravellouge/$', SpecificTravellougeAPI.as_view()),
]