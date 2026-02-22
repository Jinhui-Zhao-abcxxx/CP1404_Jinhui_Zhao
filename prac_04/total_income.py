"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    months_number = int(input("How many months? "))
    total = 0
    for month in range(1, months_number + 1):
        income_per_month = float(input(f"Enter income for month {month}: "))
        incomes.append(income_per_month)
    print("\nIncome Report\n-------------")
    for month in range(1, months_number + 1):
        total,income = calculate_report(incomes, month, total)
        print(f"Month  {month} - Income: $  {income:.2f}   Total: $  {total:.2f}")


def calculate_report(incomes, month, total):
    income = incomes[month - 1]
    total += income
    return total,income






main()