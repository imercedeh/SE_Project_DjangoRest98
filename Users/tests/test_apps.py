from django.apps import AppConfig
from django.apps import apps
from django.test import TestCase
from Users.apps import UsersConfig

class ReportConfig(TestCase):
    def test_place_app(self):
        self.assertEqual(UsersConfig.name,'Users')
        self.assertEqual(apps.get_app_config('Users').name, 'Users')
