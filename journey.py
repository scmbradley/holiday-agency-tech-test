"""Provides base class for journeys."""

# Don't use these classes.
# Use AirJourney, CarJourney and FullJourney


class Journey:
    def __init__(
        self, people=1, distance=0, append_text=None, prepend_text=None, **kwargs
    ):
        """Provide base class for journeys."""
        self.people = people
        self.distance = distance
        self.legs = []
        self.prepend_text = prepend_text
        self.append_text = append_text

    def cost(self):
        """Return costs associated with the journey."""
        if self.legs:
            return sum([leg.cost() for leg in self.legs])
        else:
            return 0

    def journey_string(self):
        """Return a list of strings representing the journey."""
        js = []
        if self.prepend_text is not None:
            js.append(self.prepend_text)
        for leg in self.legs:
            js.extend(leg.journey_string())
        if self.append_text is not None:
            js.append(self.append_text)
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
        return [self.leg_string]
