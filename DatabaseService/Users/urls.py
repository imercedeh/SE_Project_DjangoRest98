from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import Signup
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    url(r'sign-up/',Signup.as_view()),
    url(r'^token/$', jwt_views.TokenObtainPairView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)