from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import GetUser,AddUser,AddLeader,GetLeader,LeadPlace,GetPlaceLeader
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    url(r'GetUser/',GetUser.as_view()),
    url(r'AddUser/',AddUser.as_view()),
    url(r'GetLeader/',GetLeader.as_view()),
    url(r'AddLeader/',AddLeader.as_view()),
    url(r'LeadPlace/',LeadPlace.as_view()),
    url(r'GetPlaceLeader/',GetPlaceLeader.as_view()),
    url(r'^token/$', jwt_views.TokenObtainPairView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)