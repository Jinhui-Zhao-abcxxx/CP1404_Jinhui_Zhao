"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: this line
    except ValueError:  # TODO - add the exception you want to catch after except
        print("Please enter a valid integer.")
    else:
        is_finished = True



print("Valid result is:", result)