"""Handles car journeys to the airport."""
from decimal import Decimal

TAXI_COST_PER_MILE = Decimal("0.40")
CAR_COST_PER_MILE = Decimal("0.20")
CAR_COST_PARKING = Decimal("3.00")
TAXI_MAX_SEATING = 4
CAR_MAX_SEATING = 4


class CarJourney:
    def __init__(
        self,
        distance,
        people,
        taxi_per_mile=TAXI_COST_PER_MILE,
        car_per_mile=CAR_COST_PER_MILE,
        car_parking=CAR_COST_PARKING,
        taxi_max=TAXI_MAX_SEATING,
        car_max=CAR_MAX_SEATING,
    ):
        self.distance = distance
        self.people = people
        self.taxi_per_mile = taxi_per_mile
        self.car_per_mile = car_per_mile
        self.car_parking = car_parking
        self.car_type, self.cost, self.car_number = self.transit_choice()

    @staticmethod
    def _journey_string(car_type, cost, car_number):
        add_s = "s" if car_number > 1 else ""
        return f"Travel using {car_number} {car_type}{add_s} for £{cost}."

    def __str__(self):
        return CarJourney._journey_string(self.car_type, self.cost, self.car_number)

    @staticmethod
    def _journey_cost(distance, per_mile, parking):
        return distance * per_mile + parking

    def taxi_cost(
        self,
    ):
        """Calculate cost of one taxi journey."""
        return CarJourney._taxi_cost(self.distance, self.taxi_per_mile, 0)

    def car_cost(
        self,
    ):
        """Calculate cost of one car journey."""
        return CarJourney._journey_cost(
            self.distance, self.car_per_mile, self.car_parking
        )

    @staticmethod
    def _required_vehicles(people, vehicle_max):
        return (people // vehicle_max) + (people % vehicle_max > 0)

    def transit_choice(self):
        """Return the type and cost of the cheaper journey to the airport."""
        required_taxis = CarJourney._required_vehicles(self.people, self.taxi_max)
        required_cars = CarJourney._required_vehicles(self.people, self.car_max)
        taxi_cost = required_taxis * self.taxi_cost()
        car_cost = required_cars * self.car_cost()
        if car_cost > taxi_cost:
            return "Taxi", taxi_cost, required_taxis
        else:
            return "Car", car_cost, required_cars
