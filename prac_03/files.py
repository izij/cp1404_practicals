# Question 1
name = input("Name? ")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt", 'r')
name = in_file.read().strip()
in_file.close()
print(f"Your name is {name}")

# Question 3
in_file = open("numbers.txt", 'r')
line_1 = int(in_file.readline())
line_2 = int(in_file.readline())
in_file.close()
result = line_1 + line_2
print(result)

# Question 4
total = 0
in_file = open("numbers.txt", 'r')
for line in in_file:
    number = int(line)
    total = total + number
print(total)
