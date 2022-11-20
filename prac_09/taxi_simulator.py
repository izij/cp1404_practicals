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
    total_bill = 0
    print("Let's drive!")
    print(MENU_STRING)
    menu_choice = input(">>> ").lower()
    while menu_choice != 'q':
        if menu_choice == 'c':
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = get_valid_integer("Choose taxi: ")
            if taxi_choice < 0 or taxi_choice > len(taxis) - 1:
                print("Invalid taxi choice")
            else:
                current_taxi = taxis[taxi_choice]
        elif menu_choice == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()  # Start new fare for that taxi
                distance = get_valid_integer("Drive how far? ")
                current_taxi.drive(distance)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU_STRING)
        menu_choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis()


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
    for taxi in taxis:
        print(f"{taxis.index(taxi)} - {taxi}")


main()
