"""Handles connecting to the airport API."""

import requests
from decimal import Decimal

from airjourney import AirJourney

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
        self._api_airports()

    def _api_airports(self):
        self.airport_names_dict = {}
        airports_json = requests.get(self.api_url).json()
        for airport in airports_json:
            self.airport_names_dict[airport["id"]] = airport["name"]

    def airport_name(self, code):
        """Return the name of the airport from the three letter code."""
        return self.airport_names_dict[code]

    def _get_journey_json(self, origin, destination):
        return requests.get(f"{API_URL}/{origin}/to/{destination}").json()

    def get_journey(self, origin, destination):
        """Get a journey object from origin and destination."""
        return AirJourney(self._get_journey_json(origin, destination))
