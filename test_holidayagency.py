import pytest

from journey import Journey, Leg

import json
from airports import Airports
from airjourney import AirJourney
from carjourney import CarJourney, CarType
from fulljourney import FullJourney
from decimal import Decimal

# Setup fixtures

with open("airport_test.json") as f:
    airport_json = json.load(f)


@pytest.fixture
def t_journey():
    return Journey()


@pytest.fixture
def t_airport():
    return Airports()


@pytest.fixture
def t_airjourney(t_airport):
    return AirJourney(2, airport_json, t_airport)


# Tests


class TestJourney:
    def test_cost(self, t_journey):
        t_journey.add_leg(Leg(leg_cost=10))
        assert t_journey.cost() == 10

    def test_journey_string(self, t_journey):
        t_journey.add_leg(Leg(leg_string="TEST"))
        assert t_journey.journey_string() == ["TEST"]

    def test_flat_journey_string(self):
        j1 = Journey()
        j1.add_leg(Leg(leg_string="ONE"))
        j1.add_leg(Leg(leg_string="TWO"))
        j2 = Journey()
        j2.add_leg(Leg(leg_string="THREE"))
        j = Journey()
        j.add_leg(j1)
        j.add_leg(j2)
        assert j.journey_string() == ["ONE", "TWO", "THREE"]


class TestAirports:
    def test_airports_default_init(self, t_airport):
        assert t_airport.per_mile == Decimal("0.10")

    def test_airport_name(self, t_airport):
        assert t_airport.airport_name("ATH") == "Athens International Airport"
        assert (
            t_airport.airport_name("ATH", with_code=True)
            == "Athens International Airport (ATH)"
        )


class TestAirJourney:
    def test_airjourney(self, t_airjourney):
        assert t_airjourney.legs[0].origin == "ATH"

    def test_airjourney_cost(self, t_airjourney):
        assert t_airjourney.cost() == Decimal("190")


class TestCarJourney:
    def test_required_cars(self):
        assert CarJourney._required_vehicles(4, 4) == 1
        assert CarJourney._required_vehicles(4, 5) == 1
        assert CarJourney._required_vehicles(5, 5) == 1
        assert CarJourney._required_vehicles(6, 5) == 2

    def test_transit_choice(self):
        assert CarJourney.transit_choice(4, 1).car_type == CarType.TAXI
        assert CarJourney.transit_choice(4, 100).car_type == CarType.CAR

    def test_car_distance(self):
        assert CarJourney.transit_choice(6, 100).total_distance() == 100


class TestFullJourney:
    def test_full_journey(self):
        f = FullJourney(6, 100, "ATH", "SVO")
        # (100 * .2  + 3)*2 for car transit
        # 95*6 for outbound air travel
        # 101.5 *6 for return
        assert f.cost() == Decimal("1225.00")

    def test_journey_from_docs(self):
        f = FullJourney(6, 198, "LHR", "FCO")
        # Leg 0 is car journey, leg 1 is outbound, leg 2 is return.
        assert f.legs[1].legs[0].destination == "CDG"
        assert f.legs[1].legs[1].destination == "ZRH"
        assert f.legs[1].total_distance() == 320
        assert f.legs[2].legs[0].destination == "AMS"
        assert f.legs[2].total_distance() == 595
