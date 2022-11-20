"""
CP1404 Practical 9
Silver Service Taxi Class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of Taxi that changes price_per_km based on fanciness"""
    flagfall = 4.50

    def __init__(self, fuel, name, fanciness=0.0):
        """Initialise SilverServiceTaxi class based on Taxi parent class."""
        super().__init__(fuel, name)
        self.price_per_km = super().price_per_km * fanciness

    def __str__(self):
        """Return a string like Taxi but with flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Calculates fare like Taxi, but adds flagfall"""
        return super().get_fare() + self.flagfall
