"""
Prac 07 'More Guitars!' exercise
"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)


def display_guitars(guitars):
    for guitar in guitars:
        print(guitar)


def load_guitars(filename):
    """Loads Guitars from file and adds to list"""
    guitars = []
    in_file = open(filename, "r")
    in_file.readline()  # Reads header line
    for line in in_file:
        pieces = line.strip().split(",")
        guitar = Guitar(pieces[0], int(pieces[1]), float(pieces[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


main()
