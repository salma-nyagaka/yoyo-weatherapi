import json
import pytest

from locations.apps import LocationsConfig
from .base_file import BaseTestCase


class LocationsConfigTest(BaseTestCase):
    def test_apps(self):
        self.assertEqual(LocationsConfig.name, 'locations')
