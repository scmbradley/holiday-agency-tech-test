import pytest

from journey import Journey, Leg

import json
from airports import COST_PER_MILE, Airports
from airjourney import AirJourney
from carjourney import CarJourney, CarType
from fulljourney import FullJourney
from decimal import Decimal


### TODO
# Fixtures
# Parameterised tests


class TestJourney:
    def test_cost(self):
        j = Journey()
        j.add_leg(Leg(leg_cost=10))
        assert j.cost() == 10

    def test_journey_string(self):
        j = Journey()
        j.add_leg(Leg(leg_string="TEST"))
        assert j.journey_string() == ["TEST"]


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
        a = AirJourney(1, airport_json, COST_PER_MILE)
        assert a.legs[0].origin == "ATH"

    def test_airjourney_cost(self):
        a = AirJourney(2, airport_json, COST_PER_MILE)
        assert a.cost() == Decimal("190")


class TestCarJourney:
    def test_required_cars(self):
        assert CarJourney._required_vehicles(4, 4) == 1
        assert CarJourney._required_vehicles(4, 5) == 1
        assert CarJourney._required_vehicles(5, 5) == 1
        assert CarJourney._required_vehicles(6, 5) == 2

    def test_transit_choice(self):
        assert CarJourney.transit_choice(4, 1).car_type == CarType.TAXI
        assert CarJourney.transit_choice(4, 100).car_type == CarType.CAR


class TestFullJourney:
    def test_full_journey(self):
        f = FullJourney(6, 100, "ATH", "SVO")
        # (100 * .2  + 3)*2 for car transit
        # 95*6 for outbound air travel
        # 101.5 *6 for return
        assert f.cost() == Decimal("1225.00")
