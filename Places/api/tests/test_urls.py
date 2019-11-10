from django.test import SimpleTestCase
from django.urls import reverse,resolve
from Places.api import urls
from Places.api.views import CreatePlaceAPIView,ViewPlaceAPI,UniquePlaceAPI,RandomPlaces


class TestUrls(SimpleTestCase):

    def test_create_url_resolved(self):
        url=reverse('create')
        self.assertEquals(resolve(url).func.view_class,CreatePlaceAPIView)

    def test_view_url_resolved(self):
        url=reverse('View')
        self.assertEquals(resolve(url).func.view_class,ViewPlaceAPI)

    def test_uniqueplace_url_resolved(self):
        url=reverse('unique')
        self.assertEquals(resolve(url).func.view_class,UniquePlaceAPI)

    def test_randomplace_url_resolved(self):
        url=reverse('random')
        self.assertEquals(resolve(url).func.view_class,RandomPlaces)
