"""Handles creating an airplane journey."""

from journey import Journey


class AirJourney(Journey):
    def __init__(self, people, journey_json, airports):
        """Create air journey from JSON output."""
        super().__init__(people)
        stops = journey_json["journey"]
        distances = journey_json["miles"]
        for origin, destination, distance in zip(stops[:-1], stops[1:], distances):
            self.add_leg(AirLeg(people, distance, origin, destination, airports))
        self.origin = stops[0]
        self.destination = stops[-1]
        self.airports = airports
        self.prepend_text = f"Your journey from {self.airports.airport_name(self.origin,with_code=True)} to {self.airports.airport_name(self.destination,with_code=True)}:"


class AirLeg(Journey):
    def __init__(self, people, distance, origin, destination, airports):
        super().__init__(people, distance)
        self.origin = origin
        self.destination = destination
        self.airports = airports

    def cost(self):
        return self.distance * self.people * self.airports.per_mile

    def journey_string(self):
        return [
            f"Travel from {self.airports.airport_name(self.origin,with_code=True)} to {self.airports.airport_name(self.destination,with_code=True)} ({self.distance} miles)"
        ]
