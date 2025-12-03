from src.core.base_controller import BaseController

class FakeDatabase:
    def __init__(self):
        self.saved = []

    def save(self, device_id, value):
        self.saved.append((device_id, value))

class FakeDevice:
    def __init__(self, device_id, value):
        self.device_id = device_id
        self.value = value

    def read(self):
        return self.value

def test_controller_polls_and_saves_data():
    fake_db = FakeDatabase()
    controller = BaseController(fake_db)

    device = FakeDevice("temp-1", 25.5)
    controller.register_device(device)

    controller.poll_devices()

    assert fake_db.saved == [("temp-1", 25.5)]
