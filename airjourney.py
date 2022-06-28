"""Handles creating an airplane journey."""


class AirJourney:
    def __init__(self, journey_json, people, per_mile):
        """Create air journey from JSON output."""
        stops = journey_json["journey"]
        distances = journey_json["miles"]
        self.legs = list(zip(stops[:-1], stops[1:], distances))
        self.people = people
        self.per_mile = per_mile
        self.origin = stops[0]
        self.destination = stops[-1]

    def __str__(self):
        return "/n".join(AirJourney.leg_to_strings(self.legs))

    @staticmethod
    def leg_to_strings(legs):
        """Take a list of legs and return a list of strings."""
        return ["Travel from {} to {} ({} miles).".format(*leg) for leg in legs]

    def list_of_legs(self):
        return AirJourney.leg_to_strings(self.legs)

    def journey_string(self, direction="outbound"):
        return [
            f"Your {direction} journey from {self.origin} to {self.destination} (£{self.cost()})."
        ] + self.list_of_legs()

    @staticmethod
    def _cost(legs, people, per_mile):
        return sum([x[2] for x in legs]) * people * per_mile

    def cost(self):
        """Return cost of journey."""
        return AirJourney._cost(self.legs, self.people, self.per_mile)
