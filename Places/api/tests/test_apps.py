from django.apps import AppConfig
from django.apps import apps
from django.test import TestCase
from Places.apps import PlacesConfig

class ReportConfig(TestCase):
    def test_place_app(self):
        self.assertEqual(PlacesConfig.name,'Places')
        self.assertEqual(apps.get_app_config('Places').name, 'Places')
