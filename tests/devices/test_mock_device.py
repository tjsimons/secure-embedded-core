import pytest

class FakeDevice:
    def __init__(self, device_id, value):
        self.device_id = device_id
        self.value = value

    def read(self):
        return self.value

@pytest.mark.parametrize("value", [0.0, 25.5, 99.9])
def test_device_reads_multiple_values(value):
    device = FakeDevice("sensor-1", value)
    assert device.read() == value
