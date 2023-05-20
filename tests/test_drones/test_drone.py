from tests.test_setup import TestSetup
from tests.test_drones.drones_factory import DroneFactory
from rest_framework import status 

class DroneTests(TestSetup):

    def tests_register_drone(self):
        drone = DroneFactory().build_drone()
        response = self.client.post(
            '/drones/drone/',
            drone,
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data.get("serial_number"), drone["serial_number"])