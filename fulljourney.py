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
        self.airports = Airports(people)
        self.air_journey = self.airports.get_journey(origin, destination)
        self.total_cost = self.car_journey.cost + self.air_journey.cost()
