# Question 1
name = input("Name? ")

out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

# Question 2
in_file = open("name.txt", 'r')
name = in_file.read()
in_file.close()
name = name.strip()
print(f"Your name is {name}")

# Question 3
in_file = open("numbers.txt", 'r')
line_1 = in_file.readline()
line_2 = in_file.readline()
in_file.close()
result = int(line_1) + int(line_2.strip())
print(result)

