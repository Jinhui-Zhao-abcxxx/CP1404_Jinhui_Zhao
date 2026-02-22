import random
RANDOM_START = 1
RANDOM_END = 45
NUMBER_RANDOM_NUMBER = 6


def get_picks():
    for i in range(picks_number):
        picks = []
        for number in range(NUMBER_RANDOM_NUMBER):
            new_number = random.randint(RANDOM_START, RANDOM_END)
            while new_number in picks:
                new_number = random.randint(RANDOM_START, RANDOM_END)
            picks.append(new_number)
        sorted_picks = sorted(picks)
        for number in sorted_picks:
            print(f"{number:>2}",end= " ")
        print()

picks_number = int(input("How many quick picks?"))
get_picks()

