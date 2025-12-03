class BaseController:
    def __init__(self, db):
        self.devices = []
        self.db = db

    def register_device(self, device):
        self.devices.append(device)

    def poll_devices(self):
        for device in self.devices:
            value = device.read()
            self.db.save(device.device_id, value)
