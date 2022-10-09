FILENAME = "subject_data.txt"


def main():
    data = get_data()
    for line in data:
        print(f"{line[0]} is taught by {line[1]:12} and has {line[2]:3} students")


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    data_lists = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        data_lists.append(parts)
    return data_lists
    input_file.close()


main()
