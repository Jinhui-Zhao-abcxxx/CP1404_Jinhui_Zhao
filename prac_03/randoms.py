import random
def main():
    number_low,number_high =get_numbers()
    while number_high <= number_low:
        print("invalid number")
        get_numbers()
    random_number = random.randint(number_low,number_high)
    print(":)" * random_number)

def get_numbers():
    number_low = int(input("enter a lower number:"))
    number_high = int(input("enter a higher number than the number you just input:"))
    return number_low,number_high

print(f" a random number between 1 and 100 inclusive {random.randint(1, 100)}")