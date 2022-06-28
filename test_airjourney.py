import pytest
import json
from airjourney import AirJourney
from airports import COST_PER_MILE
from decimal import Decimal

with open("airport_test.json") as f:
    airport_json = json.load(f)


def test_airjourney():
    a = AirJourney(airport_json, 1, COST_PER_MILE)
    assert list(a.legs)[0] == ("ATH", "IST", 150)


def test_airjourney_cost():
    a = AirJourney(airport_json, 2, COST_PER_MILE)
    assert a.cost() == Decimal("190")
