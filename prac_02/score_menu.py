MENU = "(I)nput score\n" \
       "(D)etermine result\n" \
       "(P)rint stars\n" \
       "(Q)uit"


def main():
    """Menu function"""
    score = 0
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "I":
            score = get_valid_score(0, 100)
        elif choice == "D":
            print(determine_result(score))
        elif choice == "P":
            print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper
    print("Thank you")


def get_valid_score(min, max):
    """Returns valid score within range"""
    score = int(input("Score: "))
    while score < min or score > max:
        print("Invalid Score")
        score = int(input("Score: "))
    return score


def determine_result(score):
    """Determines result based on score out of 100"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_stars(amount):
    """Prints string of stars"""
    for star in range(amount):
        print("*", end="")


main()
