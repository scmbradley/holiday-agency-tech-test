import pytest
import json
from airjourney import AirJourney
from airports import COST_PER_MILE, Airports
from decimal import Decimal

with open("airport_test.json") as f:
    airport_json = json.load(f)


class TestAirports:
    def test_airports_default_init(self):
        a = Airports(1)
        assert a.per_mile == Decimal("0.10")

    def test_airport_name(self):
        a = Airports(1)
        assert a.airport_name("ATH") == "Athens International Airport"


class TestAirJourney:
    def test_airjourney(self):
        a = AirJourney(airport_json, 1, COST_PER_MILE)
        assert list(a.legs)[0] == ("ATH", "IST", 150)

    def test_airjourney_cost(self):
        a = AirJourney(airport_json, 2, COST_PER_MILE)
        assert a.cost() == Decimal("190")
