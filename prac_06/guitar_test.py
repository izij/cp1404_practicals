"""Test program for guitar class"""

from guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1000000)
    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age(2022)}")
    print(f"{another_guitar.name} get_age() - Expected 9. Got {another_guitar.get_age(2022)}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage(2022)}")
    print(f"{another_guitar.name} is_vintage() - Expected False. Got {another_guitar.is_vintage(2022)}")



main()
