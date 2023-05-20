# UNRELIABLE CAR

import random

from Car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        """Return a string representation of the car's details."""
        return f"Car: {self.name}, Fuel: {self.fuel}, Reliability: {self.reliability}"

    def drive(self, distance):
        """Drive like parent Car but only if a random number is less than the car's reliability."""
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven
