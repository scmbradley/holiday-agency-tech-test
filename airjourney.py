"""Handles creating an airplane journey."""

from journey import Journey


class AirJourney(Journey):
    def __init__(self, people, journey_json, per_mile):
        """Create air journey from JSON output."""
        super().__init__(people)
        stops = journey_json["journey"]
        distances = journey_json["miles"]
        for origin, destination, distance in zip(stops[:-1], stops[1:], distances):
            self.add_leg(AirLeg(people, distance, origin, destination, per_mile))
        self.per_mile = per_mile
        self.origin = stops[0]
        self.destination = stops[-1]


class AirLeg(Journey):
    def __init__(self, people, distance, origin, destination, per_mile):
        super().__init__(people, distance)
        self.origin = origin
        self.destination = destination
        self.per_mile = per_mile

    def cost(self):
        return self.distance * self.people * self.per_mile

    def journey_string(self):
        return (
            f"Travel from {self.origin} to {self.destination} ({self.distance} miles)"
        )
