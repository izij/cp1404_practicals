"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.

I had to remove prac_06 because it wasn't recognised. I'm not sure why because that is my folder name.
"""

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180, "My car")
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car(100, "Limo")
    limo.add_fuel(20)
    print(f"Limo has fuel: {limo.fuel}")
    limo.drive(115)
    print(limo)


main()
