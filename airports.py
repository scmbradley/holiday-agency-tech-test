"""Handles connecting to the airport API."""

import requests
from decimal import Decimal

COST_PER_MILE = Decimal("0.10")

API_URL = "https://7302htasp6.execute-api.eu-west-1.amazonaws.com/v1/airport"


class Airports:
    """Provide starting point for journey requests."""

    def __init__(
        self,
        api_url=API_URL,
        per_mile=COST_PER_MILE,
    ):
        self.api_url = api_url
        self.per_mile = per_mile
        self._get_airports()

    def _get_airports(self):
        self.airport_names_dict = {}
        airports_json = requests.get(self.api_url).json()
        for airport in airports_json:
            self.airport_names_dict[airport["id"]] = airport["name"]

    def airport_name(self, code):
        return self.airport_names_dict[code]


def get_journey(origin, destination, verbose=False):
    """Request journey from API."""
    response = requests.get(f"{API_URL}/{origin}/to/{destination}")
    stops = response.json()["journey"]
    distances = response.json()["miles"]
    if verbose:
        print_journey(stops, distances)
    return stops, distances
