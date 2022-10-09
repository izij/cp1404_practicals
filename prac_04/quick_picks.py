import random

NUMBER_MINIMUM = 1
NUMBER_MAXIMUM = 45
NUMBER_OF_NUMBERS = 6
quick_picks = []

number_picks = int(input("How many quick picks? "))

for i in range(number_picks):
    quick_pick = []
    for number in range(1, NUMBER_OF_NUMBERS):
        number = random.randint(NUMBER_MINIMUM, NUMBER_MAXIMUM)
        quick_pick.append(number)

    quick_picks.append(quick_pick)
print(quick_picks)
