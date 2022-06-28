import pytest
import json
from airports import COST_PER_MILE, Airports
from airjourney import AirJourney
from carjourney import CarJourney
from fulljourney import FullJourney
from decimal import Decimal


### TODO
# Fixtures
# Parameterised tests


with open("airport_test.json") as f:
    airport_json = json.load(f)


class TestAirports:
    def test_airports_default_init(self):
        a = Airports()
        assert a.per_mile == Decimal("0.10")

    def test_airport_name(self):
        a = Airports()
        assert a.airport_name("ATH") == "Athens International Airport"


class TestAirJourney:
    def test_airjourney(self):
        a = AirJourney(airport_json, 1, COST_PER_MILE)
        assert a.legs[0] == ("ATH", "IST", 150)

    def test_airjourney_cost(self):
        a = AirJourney(airport_json, 2, COST_PER_MILE)
        assert a.cost() == Decimal("190")

    def test_leg_to_strings(self):
        a = AirJourney(airport_json, 1, COST_PER_MILE)
        assert (
            AirJourney.leg_to_strings(a.legs)[0]
            == "Travel from ATH to IST (150 miles)."
        )


class TestCarJourney:
    def test_required_cars(self):
        assert CarJourney._required_vehicles(4, 5) == 1
        assert CarJourney._required_vehicles(5, 5) == 1
        assert CarJourney._required_vehicles(6, 5) == 2

    def test_taxi_cost(self):
        c = CarJourney(30, 2)
        assert c.taxi_cost() == Decimal("12.00")


class TestFullJourney:
    def test_full_journey(self):
        f = FullJourney(100, 6, "ATH", "SVO")
        assert f.car_journey.car_type == "Car"
        # (100 * .2  + 3)*2 for car transit
        # 95*6 for outbound air travel
        # 101.5 *6 for return
        assert f.total_cost == Decimal("1225.00")
