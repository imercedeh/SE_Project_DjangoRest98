from django.conf.urls import include, url
from rest_framework.authtoken import views
from Users.views import Signup,Login,LeaderCreation
from rest_framework import routers
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
#router = routers.DefaultRouter()


urlpatterns = [
    url(r'^sign-up/$', Signup.as_view()),
     url(r'^token/$',Login.as_view()),
     url(r'^leadercreation/$', LeaderCreation.as_view()),
    # url(r'^me/$', ProfileAPI.as_view()),
    # url(r'SpecificLeader/',SpecificLeaderAPI.as_view()),
    # url(r'SpecificUser/',SpecificUserAPI.as_view()),
    # url(r'LeadPlace/',LeadPlaceAPI.as_view()),
    # url(r'ChangeAvailability/',ChangeAvailabilityAPI.as_view()),
    # url('LeadersView/',LeadersView.as_view(),name='LeadersView'),
    # url('LeaderSortView/',LeaderSortView.as_view(),name='LeaderSortView'),
    # url('LeaderAdvanceSearch/',LeaderAdvanceSearch.as_view({'get': 'list'}),name='LeaderAdvanceSearch'),
    # url('UserAdvanceSearch/',UserAdvanceSearch.as_view({'get': 'list'}),name='UserAdvanceSearch'),
    # url('UsersView/',UsersView.as_view(),name='UsersView'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)