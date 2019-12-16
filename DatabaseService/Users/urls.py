from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import Signup

urlpatterns = [
    url(r'sign-up/',Signup.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)