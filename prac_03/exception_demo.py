"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
When user enter a value can't be integer like string or float.
2. When will a ZeroDivisionError occur?
When user enter integer in both numerator and denominator but enter 0 in denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Solution has been provided below.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    while denominator == 0:
        print("Please enter a number not zero")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")