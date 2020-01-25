from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Places.views import CreatePlace,UniquePlace,RandomPlaces
urlpatterns = [
    url(r'CreatePlace/', CreatePlace.as_view(), name='create'),  
    url(r'UniquePlace/',UniquePlace.as_view(),name='unique'),  
    url(r'RandomPlace/',RandomPlaces.as_view(),name='random'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)