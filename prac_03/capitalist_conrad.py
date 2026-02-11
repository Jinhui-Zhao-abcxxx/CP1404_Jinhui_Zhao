import random


STARTING_PRICE = 10.00

MAX_INCREASE_RATE = 0.1
MAX_DECREASE_RATE = 0.05
MAX_STOP_POINT = 1000.00
MIN_STOP_POINT = 0.01


def main():
    price = STARTING_PRICE
    print(f"starting price: ${price}")
    number_of_days = 0
    out_file = open("output.txt", "w")
    while MAX_STOP_POINT > price > MIN_STOP_POINT:
        number_of_days += 1
        if is_increase():
            price += price * random.uniform(0, MAX_INCREASE_RATE)
        else:
            price -= price * random.uniform(0, MAX_DECREASE_RATE)
        print(f"On day {number_of_days} price is: ${price:.2f}",file=out_file)

    out_file.close()


def is_increase():
    """Determine whether a price increase."""
    decide_value = random.randint(0,1)
    if decide_value == 0:
        return True
    else:
        return False

main()

