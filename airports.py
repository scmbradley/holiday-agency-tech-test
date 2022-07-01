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
        air_per_mile=COST_PER_MILE,
        **kwargs,
    ):
        self.api_url = api_url
        self.per_mile = air_per_mile
        self._api_airports()

    def _api_airports(self):
        self.airport_names_dict = {}
        airports_json = requests.get(self.api_url).json()
        for airport in airports_json:
            self.airport_names_dict[airport["id"]] = airport["name"]

    def airport_name(self, code, with_code=False):
        """Return the name of the airport from the three letter code."""
        add_code = f" ({code})" if with_code else ""
        return self.airport_names_dict[code] + add_code

    def _get_journey_json(self, origin, destination):
        return requests.get(f"{API_URL}/{origin}/to/{destination}").json()

    def get_journey(self, origin, destination, people):
        """Get a journey object from origin and destination."""
        return AirJourney(people, self._get_journey_json(origin, destination), self)

    def airport_list(self, **kwargs):
        """Return a list of airport names, and a dict for getting back the code."""
        airport_list = []
        name_to_code = {}
        for k in self.airport_names_dict.keys():
            full_name = self.airport_name(k, **kwargs)
            airport_list.append(full_name)
            name_to_code[full_name] = k
        return sorted(airport_list), name_to_code
