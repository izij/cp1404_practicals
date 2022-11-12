"""
Prac 07 'More Guitars!' exercise
"""
from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    guitars = load_guitars(FILENAME)
    guitars.sort()
    display_guitars(guitars)
    choice = input("Add new guitar (Y/N)? ").upper()
    while choice != "N":
        guitar = get_new_guitar()
        guitars.append(guitar)
        print(f"{guitar.name} ({guitar.year}) : ${guitar.cost:,.2f} added.")
        choice = input("Add new guitar (Y/N)? ").upper()
    save_guitars(guitars, FILENAME)


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


def get_new_guitar():
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: $"))
    guitar = Guitar(name, year, cost)
    return guitar


def save_guitars(guitars, filename):
    """Saves guitars into a CSV file"""
    outfile = open(filename, 'w')
    for guitar in guitars:
        data = [guitar.name, str(guitar.year), str(guitar.cost)]
        print(",".join(data), file=outfile)
    outfile.close()


main()
