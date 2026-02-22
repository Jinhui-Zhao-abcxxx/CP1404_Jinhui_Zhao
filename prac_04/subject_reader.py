"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject data from file."""
    data_course = load_data(FILENAME)
    print(data_course)
    for row in data_course:
        print(f"{row[0]} is taught by {row[1]:<12} and has {row[2]:>3} students")


def load_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    data_set = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        # Make the number an integer as part of a new, poorly named, list
        data = [parts[0], parts[1], int(parts[2])]
        print(data)  # See if that worked
        data_set.append(data)
        print("----------")
    input_file.close()
    return data_set


main()