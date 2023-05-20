from apps.drones.models import Drone, Medication

class DroneFactory:

    def build_drone(self):
        return {"serial_number":"test-wg-dm-aj", "model":"Middleweight", "weight_limit":"300", "battery_capacity":"36", "status":"IDLE"}
    
    def create_drone(self):
        return Drone.objects.create(**self.build_drone())
