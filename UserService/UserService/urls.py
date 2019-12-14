"""UserService URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework.authtoken import views
from Users.views import SignupAPI,LeaderCreationAPI,ProfileAPI,SpecificLeaderAPI,SpecificUserAPI,LeadPlaceAPI,LeadersView,LeaderAdvanceSearch,LeaderSortView,UserAdvanceSearch,UsersView,ChangeAvailabilityAPI

from rest_framework import routers
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
#router = routers.DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/sign-up/$', SignupAPI.as_view()),
    url(r'^api/token/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^api/token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    url(r'^api/leadercreation/$', LeaderCreationAPI.as_view()),
    url(r'^api/me/$', ProfileAPI.as_view()),
    url(r'api/SpecificLeader/',SpecificLeaderAPI.as_view()),
    url(r'api/SpecificUser/',SpecificUserAPI.as_view()),
    url(r'api/LeadPlace/',LeadPlaceAPI.as_view()),
    url(r'api/ChangeAvailability/',ChangeAvailabilityAPI.as_view()),
    url('api/LeadersView/',LeadersView.as_view(),name='LeadersView'),
    url('api/LeaderSortView/',LeaderSortView.as_view(),name='LeaderSortView'),
    url('api/LeaderAdvanceSearch/',LeaderAdvanceSearch.as_view({'get': 'list'}),name='LeaderAdvanceSearch'),
    url('api/UserAdvanceSearch/',UserAdvanceSearch.as_view({'get': 'list'}),name='UserAdvanceSearch'),
    url('api/UsersView/',UsersView.as_view(),name='UsersView'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
