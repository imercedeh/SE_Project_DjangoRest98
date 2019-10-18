from django.conf.urls import include, url
from rest_framework.authtoken import views
from Users.views import SignupAPI

from rest_framework import routers
from rest_framework.authtoken import views
from django.conf import settings
#router = routers.DefaultRouter()


urlpatterns = [
    url(r'^sign-up/$', SignupAPI.as_view()),
]