from unittest.mock import MagicMock
from src.core.base_controller import BaseController

class FakeDevice:
    def __init__(self, device_id, value):
        self.device_id = device_id
        self.value = value

    def read(self):
        return self.value

def test_controller_calls_database_once_per_device():
    mock_db = MagicMock()
    controller = BaseController(mock_db)

    device1 = FakeDevice("d1", 10)
    device2 = FakeDevice("d2", 20)

    controller.register_device(device1)
    controller.register_device(device2)

    controller.poll_devices()

    assert mock_db.save.call_count == 2
