import re
import time
import pytest
import station1

def test_temperature_valid_range():
    t = -999
    assert station1.validate_temperature(t)

def test_temperature_failure_case():
    t = 35
    assert not station1.validate_temperature(t)

def test_humidity_range():
    h = 120
    assert station1.validate_humidity(h)

def test_humidity_failure_case():
    h = 45
    assert not station1.validate_humidity(h)