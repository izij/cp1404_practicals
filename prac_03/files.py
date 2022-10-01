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
