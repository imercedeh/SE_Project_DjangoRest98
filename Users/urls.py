from django.conf.urls import include, url
from rest_framework.authtoken import views
from Users.views import SignupAPI,UserAPI,Become_LeaderAPI,LeaderAPI

from rest_framework import routers
from rest_framework.authtoken import views
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
#router = routers.DefaultRouter()


urlpatterns = [
    url(r'^sign-up/$', SignupAPI.as_view()),
    url(r'^token/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^me/$', UserAPI.as_view()),
    url(r'^become-leader/$', Become_LeaderAPI.as_view()),
    url(r'^me/leader/$', LeaderAPI.as_view()),
]