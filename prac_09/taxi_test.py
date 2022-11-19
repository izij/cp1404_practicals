"""
CP1404 Practical 9
Test code for Taxi class
"""

from prac_09.taxi import Taxi


def run_tests():
    my_taxi = Taxi(100, "Prius 1")
    my_taxi.drive(40)
    print(my_taxi, "total fare is: $", my_taxi.get_fare())
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi, "total fare is: $", my_taxi.get_fare())


run_tests()
