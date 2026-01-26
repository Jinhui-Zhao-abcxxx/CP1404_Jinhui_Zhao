"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            print(f"Result: {convert_celsius_to_fahrenheit():.2f} F")
        elif choice == "F":
            print(f"Result: {convert_fahrenheit_to_celsius():.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")



def convert_celsius_to_fahrenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def convert_fahrenheit_to_celsius():
    fahrenheit = float(input("Fahrenheit : "))
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius

main()



