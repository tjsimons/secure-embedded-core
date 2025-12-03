import pytest
from src.core.base_controller import BaseController

class FakeDatabase:
    def __init__(self):
        self.saved = []

    def save(self, device_id, value):
        self.saved.append((device_id, value))

@pytest.fixture
def controller():
    db = FakeDatabase()
    return BaseController(db)
