import random
from src.devices.base_device import BaseDevice

class MockTempSensor(BaseDevice):
    def read(self):
        return round(random.uniform(20.0, 30.0), 2)

    def health_check(self) -> bool:
        return True
