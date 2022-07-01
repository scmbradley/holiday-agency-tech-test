"""Calculates prices and distances for requested trip."""

from journey import Journey
from carjourney import CarJourney
from airports import Airports


class FullJourney(Journey):
    def __init__(
        self, people, distance_to_airport, origin, destination, airports=None, **kwargs
    ):
        """Create a FullJourney object."""
        super().__init__(people, distance_to_airport)
        self.origin = origin
        self.destination = destination
        self.add_leg(CarJourney.transit_choice(people, distance_to_airport, **kwargs))

        if airports is None:
            self.airports = Airports(**kwargs)
        else:
            self.airports = airports
        self.add_leg(self.airports.get_journey(origin, destination, people))
        self.add_leg(self.airports.get_journey(destination, origin, people))
        self.append_text = f"Total cost: £{self.cost()}."

    def print_journey(self):
        print("\n".join(self.journey_string()))
