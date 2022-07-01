"""Handles car journeys to the airport."""
from decimal import Decimal
from enum import Enum
from journey import Journey

TAXI_COST_PER_MILE = Decimal("0.40")
CAR_COST_PER_MILE = Decimal("0.20")
CAR_COST_PARKING = Decimal("3.00")
TAXI_MAX_SEATING = 4
CAR_MAX_SEATING = 4


class CarType(Enum):
    CAR = "Car"
    TAXI = "Taxi"


class CarJourney(Journey):
    def __init__(self, people, distance, car_type, car_number, car_cost):
        """
        Create a CarJourney object.

        Do not call this directly, use the transit_choice method.
        """
        super().__init__(people, distance)
        self.car_type = car_type
        self.car_number = car_number
        self.car_cost = car_cost

    def journey_string(self):
        add_s = "s" if self.car_number > 1 else ""
        return [
            f"Travel using {self.car_number} {self.car_type.value}{add_s} for £{self.cost()}."
        ]

    def cost(self):
        return self.car_cost

    @staticmethod
    def _journey_cost(distance, per_mile, parking):
        return (distance * per_mile) + parking

    @staticmethod
    def _required_vehicles(people, vehicle_max):
        return (people // vehicle_max) + (people % vehicle_max > 0)

    @staticmethod
    def transit_choice(
        people,
        distance,
        taxi_per_mile=TAXI_COST_PER_MILE,
        car_per_mile=CAR_COST_PER_MILE,
        car_parking=CAR_COST_PARKING,
        taxi_max=TAXI_MAX_SEATING,
        car_max=CAR_MAX_SEATING,
    ):
        """Return the type and cost of the cheaper journey to the airport."""
        required_taxis = CarJourney._required_vehicles(people, taxi_max)
        required_cars = CarJourney._required_vehicles(people, car_max)
        taxi_cost = required_taxis * CarJourney._journey_cost(
            distance, taxi_per_mile, 0
        )
        car_cost = required_cars * CarJourney._journey_cost(
            distance, car_per_mile, car_parking
        )
        if car_cost > taxi_cost:
            return CarJourney(people, distance, CarType.TAXI, required_taxis, taxi_cost)
        else:
            return CarJourney(people, distance, CarType.CAR, required_cars, car_cost)
