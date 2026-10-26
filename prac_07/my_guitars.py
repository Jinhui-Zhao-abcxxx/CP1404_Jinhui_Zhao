from guitar import Guitar


def main():

    in_file = open("guitars.csv", "r")
    in_file.readline()

    my_guitars = []

    for line in in_file:
        guitar = (line.strip().split(","))
        my_guitar = Guitar(guitar[0], int(guitar[1]), float(guitar[2]))
        my_guitars.append(my_guitar)

    my_guitars.sort()

    for guitar in my_guitars:
        print(guitar)

main()

