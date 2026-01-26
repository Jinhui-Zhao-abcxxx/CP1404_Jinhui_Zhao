"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random


def main():
    score = float(input('Enter your score: '))
    grade = determine_grade(score)
    print(f"Your grade is {grade}")
    random_number = random.randint(0,101)
    print(f"random: {random_number} = {determine_grade(random_number)}")


def determine_grade(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()

