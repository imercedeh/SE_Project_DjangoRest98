from django.conf.urls import include, url
from rest_framework.authtoken import views

from rest_framework import routers
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
from Gate.views import(Signup,Login,LeaderCreation,LeadPlace,ChangeAvailability)
from rest_framework_simplejwt import views as jwt_views
#router = routers.DefaultRouter()


urlpatterns = [
     url(r'^sign-up/$',Signup.as_view()),
     url(r'^token/$', Login.as_view()),
     url(r'^leadercreation/$', LeaderCreation.as_view()),
    # url(r'^me/$', ProfileAPI.as_view()),
    # url(r'SpecificLeader/',SpecificLeaderAPI.as_view()),
    # url(r'SpecificUser/',SpecificUserAPI.as_view()),
     url(r'LeadPlace/',LeadPlace.as_view()),
    url(r'ChangeAvailability/',ChangeAvailability.as_view()),
    # url('LeadersView/',LeadersView.as_view(),name='LeadersView'),
    # url('LeaderSortView/',LeaderSortView.as_view(),name='LeaderSortView'),
    # url('LeaderAdvanceSearch/',LeaderAdvanceSearch.as_view({'get': 'list'}),name='LeaderAdvanceSearch'),
    # url('UserAdvanceSearch/',UserAdvanceSearch.as_view({'get': 'list'}),name='UserAdvanceSearch'),
    # url('UsersView/',UsersView.as_view(),name='UsersView'),
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)