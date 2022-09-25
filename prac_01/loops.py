for i in range(1, 21, 2):
    print(i, end=' ')
print()

# a.
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# b.
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# c.
number_stars = int(input("Number of stars: "))
for star in range(number_stars):
    print("*", end='')

# d.
for star in range(number_stars+1):
    print("*" * star)
