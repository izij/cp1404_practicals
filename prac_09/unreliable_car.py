"""
CP1404 Practical 09
Unreliable Car Class
"""
import random

from prac_09.car import Car
from random import randint


class UnreliableCar(Car):
    """Specialised version of Car that includes reliability"""

    def __init__(self, fuel, name, reliability=0):
        super().__init__(fuel, name)
        self.reliability = reliability

    def __str__(self):
        """Return a string like a Car, but add reliability"""
        return f"{super().__str__()}, reliability of {self.reliability}"

    def drive(self, distance):
        if randint(0, 100) < self.reliability:
            return super().drive(distance)
        else:
            return 0
