from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from django.test import TestCase
from Places.models import Places
from Users.models import User,Leader
from Places.api.views import UniquePlaceAPI
from rest_framework.test import APIRequestFactory
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet 
