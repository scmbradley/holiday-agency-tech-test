import pytest
from airports import Airports
from decimal import Decimal


def test_airports_default_init():
    a = Airports(1)
    assert a.per_mile == Decimal("0.10")


def test_airport_name():
    a = Airports(1)
    assert a.airport_name("ATH") == "Athens International Airport"
