from src.devices.base_device import BaseDevice

class BaseController:
    def __init__(self):
        self.devices: list[BaseDevice] = []

    def register_device(self, device: BaseDevice):
        self.devices.append(device)

    def poll_devices(self):
        results = {}
        for device in self.devices:
            results[device.device_id] = device.read()
        return results
