from django.conf.urls import include, url
from rest_framework.authtoken import views


from rest_framework import routers
from rest_framework.authtoken import views
from django.conf import settings
from rest_framework_simplejwt import views as jwt_views
#router = routers.DefaultRouter()


urlpatterns = [
    url(r'^token/$', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r'^token/refresh/$', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]