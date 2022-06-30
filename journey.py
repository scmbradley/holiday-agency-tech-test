"""Provides base class for journeys."""

# Don't use these classes.
# Use AirJourney, CarJourney and FullJourney


class Journey:
    def __init__(self, people=1, distance=0, **kwargs):
        """Provide base class for journeys."""
        self.people = people
        self.distance = distance
        self.legs = []

    def cost(self):
        """Return costs associated with the journey."""
        if self.legs:
            return sum([leg.cost() for leg in self.legs])
        else:
            return 0

    def journey_string(self):
        js = []
        for leg in self.legs:
            js.extend([leg.journey_string()])
        return js

    def add_leg(self, leg):
        """Add leg to journey."""
        self.legs.append(leg)


# Especially don't use this class.
# Subclass the above classes.
# This is an example, for testing purposes only.


class Leg(Journey):
    def __init__(self, people=1, leg_cost=0, leg_string="STRING"):
        super().__init__(people)
        self.leg_cost = leg_cost
        self.leg_string = leg_string

    def cost(self):
        return self.leg_cost

    def journey_string(self):
        return self.leg_string
