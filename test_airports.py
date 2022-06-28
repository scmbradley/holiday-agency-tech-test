import pytest
from airports import Airports
from decimal import Decimal


def test_airports_default_init():
    a = Airports()
    assert a.per_mile == Decimal("0.10")
