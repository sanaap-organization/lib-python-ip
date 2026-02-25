import pytest
from lib_python_ip.core import IPDetector


@pytest.fixture
def detector():
    networks = [
        "5.52.0.0/16",
        "2.144.0.0/14"
    ]
    return IPDetector(networks)


def test_ip_inside_range(detector):
    assert detector.check("5.52.10.20") is True


def test_ip_outside_range(detector):
    assert detector.check("8.8.8.8") is False


def test_exact_boundary_ip(detector):
    assert detector.check("5.52.0.0") is True


def test_invalid_ip_format(detector):
    with pytest.raises(ValueError):
        detector.check("not-an-ip")
