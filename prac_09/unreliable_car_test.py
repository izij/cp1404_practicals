"""
CP1404 Practical 09
Test code for Unreliable Car Class
"""
from prac_09.unreliable_car import UnreliableCar


def run_tests():
    my_car = UnreliableCar(100, "My Car", 50)
    my_car.drive(20)
    print(my_car)
    my_car.drive(30)
    print(my_car)


run_tests()
