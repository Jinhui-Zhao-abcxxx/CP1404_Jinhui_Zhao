from prac_06.guitar import Guitar

print("My guitars!")
guitars = []

name = input("Name:")

while name != "":
    year = int(input("Year:"))
    cost = float(input("Cost:$"))
    guitars.append(Guitar(name,year,cost))
    name = input("Name:")

# i = 0
# for guitar in guitars:
#     i += 1
for i, guitar in enumerate(guitars, 1):
# do something with i (the index) and guitar (the element)
    if guitar.is_vintage():
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")





