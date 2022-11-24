"""
CP1404 Practical 9
Silver Service Taxi text code
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def run_tests():
    fancy_taxi = SilverServiceTaxi(200, "Hummer", 4)
    print(fancy_taxi)
    expensive_taxi = SilverServiceTaxi(100, "Silver Cab", 2)
    expensive_taxi.drive(18)
    print(f"{expensive_taxi}, fare of ${expensive_taxi.get_fare():.2f}")


run_tests()
