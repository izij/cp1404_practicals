"""
Guitars!
Estimate time: 40 min
Actual time: 42 min
"""


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) : ${self.cost:10,.2f}"

    def get_age(self, current_year):
        age = current_year - self.year
        return age

    def is_vintage(self, current_year):
        return self.get_age(current_year) >= 50