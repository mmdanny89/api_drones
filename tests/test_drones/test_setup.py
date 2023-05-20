from rest_framework.test import APITestCase
import json
from pathlib import Path

class TestSetup(APITestCase):
    def setUp(self):
        current_working_directory = Path.cwd()
        data = open(str(current_working_directory)+'/tests/test_drones/initial_data.json', 'r')
        data_load = json.loads(data.read())
        print(data_load)
        return super().setUp()

    def test_asds(self):
        pass