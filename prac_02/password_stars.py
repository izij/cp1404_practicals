minimum_length = int(input("Minimum length: "))
password = input("Enter password: ")

while len(password) < minimum_length:
    print("Password is not long enough")
    password = input("Enter password: ")

print("*"*len(password))