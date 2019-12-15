from django.conf.urls import include, url
from rest_framework.authtoken import views
from Gate.views import Signup

from rest_framework import routers
from rest_framework.authtoken import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
#router = routers.DefaultRouter()


urlpatterns = [
     url(r'^sign-up/$',Signup.as_view()),
    # url(r'^token/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # url(r'^token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # url(r'^leadercreation/$', LeaderCreationAPI.as_view()),
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
]#+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)