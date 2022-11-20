"""
CP1404 practical 9
Taxi Simulator program
"""
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU_STRING = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program."""
    taxis = [Taxi(100, "Prius"), SilverServiceTaxi(100, "Limo", 2), SilverServiceTaxi(200, "Hummer", 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU_STRING)
    menu_choice = input(">>> ").lower()
    while menu_choice != 'q':
        if menu_choice == 'c':
            display_taxis(taxis)
            taxi_choice = get_valid_taxi(len(taxis) - 1)
            current_taxi = taxis[taxi_choice]
        if menu_choice == 'd':
            pass
        else:
            print("Invalid option")
        print(f"Bill to date: $")
        print(MENU_STRING)
        menu_choice = input(">>> ").lower()


def get_valid_taxi(maximum):
    """Gets a taxi number within the number of taxis."""
    taxi_choice = get_valid_integer("Choose taxi:")
    while taxi_choice < 0 or taxi_choice > maximum:
        print("Invalid taxi choice")
        taxi_choice = get_valid_integer("Choose taxi:")
    return taxi_choice


def get_valid_integer(prompt):
    """Gets a valid integer."""
    is_finished = False
    while not is_finished:
        try:
            choice = int(input(prompt))
            is_finished = True
        except ValueError:
            print("Invalid choice: Please enter a valid integer")
    return choice


def display_taxis(taxis):
    """Displays list of taxis with index number"""
    print("Taxis available:")
    for taxi in taxis:
        print(taxis.index(taxi), taxi)


main()
