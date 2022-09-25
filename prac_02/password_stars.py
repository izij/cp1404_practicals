def main():
    """Main function"""
    minimum_length = int(input("Minimum length: "))
    password = get_password(minimum_length)
    print_stars(password)


def print_stars(password):
    print("*" * len(password))


def get_password(minimum_length):
    password = input("Enter password: ")
    while len(password) < minimum_length:
        print("Password is not long enough")
        password = input("Enter password: ")
    return password


main()
