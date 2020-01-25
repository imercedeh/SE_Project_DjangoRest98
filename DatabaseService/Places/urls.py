from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from .views import AddPlace,GetUniquePlace,GetRandomPlace#,AllPlace


urlpatterns = [
    url(r'AddPlace/',AddPlace.as_view()),
    url(r'GetUniquePlace/',GetUniquePlace.as_view()),
    url(r'GetRandomPlace/',GetRandomPlace.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)