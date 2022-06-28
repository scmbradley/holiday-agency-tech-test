"""Handles creating an airplane journey."""


class AirJourney:
    def __init__(self, journey_json):
        """Create air journey from JSON output."""
        stops = journey_json["journey"]
        distances = journey_json["miles"]
        self.legs = zip(stops[:-1], stops[1:], distances)

    def __str__(self):
        return "/n".join(AirJourney.leg_to_strings(self.legs))

    @staticmethod
    def leg_to_strings(legs):
        """Take a list of legs and return a list of strings."""
        return ["Travel from {} to {} ({}) miles.".format(*leg) for leg in legs]
