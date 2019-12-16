from django.conf.urls import url
from django.contrib import admin

from .views import UsersUsername

urlpatterns = [
    url(r'username/', UsersUsername.as_view(), name='get_username'), 
]