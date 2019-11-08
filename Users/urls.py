from django.conf.urls import include, url
from rest_framework.authtoken import views
from Users.views import SignupAPI,LeaderCreationAPI,ProfileAPI,SpecificLeaderAPI,SpecificUserAPI,LeadPlaceAPI

from rest_framework import routers
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
#router = routers.DefaultRouter()


urlpatterns = [
    url(r'^sign-up/$', SignupAPI.as_view()),
    url(r'^token/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^leadercreation/$', LeaderCreationAPI.as_view()),
    url(r'^me/$', ProfileAPI.as_view()),
    url(r'SpecificLeader/',SpecificLeaderAPI.as_view()),
    url(r'SpecificUser/',SpecificUserAPI.as_view()),
    url(r'LeadPlace/',LeadPlaceAPI.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)