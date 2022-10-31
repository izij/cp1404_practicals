"""
Emails
Estimate: 30 min
Actual:   50 min
"""

CONFIRM_NO = ["n", "no"]


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        name = extract_name(email).title()
        confirm = input(f"Is your name {name}? (Y/n) ").lower()
        if confirm in CONFIRM_NO:
            name = input("Name: ").title()
        email_to_name[email] = name
        email = input("Email: ")
    print()  # Empty line for formatting
    for email in email_to_name.items():
        print(f"{email[1]} ({email[0]})")


def extract_name(email):
    name = email.split("@")[0].replace(".", " ")
    return name.title()


main()
