import random

NUMBER_MINIMUM = 1
NUMBER_MAXIMUM = 45
NUMBER_OF_NUMBERS = 6

number_picks = int(input("How many quick picks? "))

for i in range(number_picks):
    quick_pick = []
    for number in range(NUMBER_OF_NUMBERS):
        number = random.randint(NUMBER_MINIMUM, NUMBER_MAXIMUM + 1)
        while number in quick_pick:
            number = random.randint(NUMBER_MINIMUM, NUMBER_MAXIMUM)
        quick_pick.append(number)
    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))

