"""
The program allows the user to enter the number of items and the price of each different item.
Then the program computes and displays the total price of those items.
If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
"""

number_of_items = int(input("Number of items: "))
total_price = 0
discount_rate = 0.9

while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for item in range(number_of_items):
    price_of_item = float(input("Price of item:$"))
    total_price += price_of_item

if total_price > 100:
    total_price = total_price * discount_rate


print(f"Total price for {number_of_items} items is ${total_price:.2f}")
