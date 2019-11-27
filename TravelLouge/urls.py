from django.conf.urls import include, url
from rest_framework.authtoken import views
from TravelLouge.views import TravelLougeCreationAPI

from rest_framework import routers
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^travellouge-creation/$', TravelLougeCreationAPI.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)