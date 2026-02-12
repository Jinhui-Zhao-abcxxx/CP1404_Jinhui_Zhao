"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

EXTRA_BONUS_RATE = 0.15
BASIC_BONUS_RATE = 0.1
TARGET_SALES = 1000
sales = float(input("Enter the sales:$ "))

while sales >= 0:

    if sales >= TARGET_SALES:
        sales_bonus = EXTRA_BONUS_RATE * sales

    else:
        sales_bonus = BASIC_BONUS_RATE * sales
    print("Your bonus is $",sales_bonus)

    sales = float(input("Enter the sales:$ "))

