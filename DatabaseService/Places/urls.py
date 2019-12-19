from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import AddPlace,GetPlace#,AllPlace


urlpatterns = [
    url(r'AddPlace/',AddPlace.as_view()),
    url(r'GetPlace/',GetPlace.as_view()),
    #url(r'AllPlace/',AllPlace.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)