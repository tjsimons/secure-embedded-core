from abc import ABC, abstractmethod

class BaseDevice(ABC):
    def __init__(self, device_id: str):
        self.device_id = device_id

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def health_check(self) -> bool:
        pass
