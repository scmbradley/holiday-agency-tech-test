"""Calculates prices and distances for requested trip."""

from carjourney import CarJourney
from airports import Airports


class FullJourney:
    def __init__(self, distance_to_airport, people, origin, destination, **kwargs):
        self.distance_to_airport = distance_to_airport
        self.people = people
        self.origin = origin
        self.destination = destination
        self.car_journey = CarJourney(distance_to_airport, people, **kwargs)
        self.airports = Airports()
        self.outbound_air_journey = self.airports.get_journey(
            origin, destination, people
        )
        self.inbound_air_journey = self.airports.get_journey(
            destination, origin, people
        )
        self.total_cost = (
            self.car_journey.cost
            + self.outbound_air_journey.cost()
            + self.inbound_air_journey.cost()
        )
