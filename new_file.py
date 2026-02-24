file = open("countries.csv")

countries = []
for line in file:
    countries.append(line.split(","))

countries.pop(0)
nations = []
capitals = []
populations = []
rates = []

for country in countries:
    country.pop(-1)
    country[2] = country[2] + country[3] + country[4]
    country.pop(3)
    country.pop(3)
    country[2] =int(country[2][1:-1])
    country[3] =float(country[3][:-1]) / 100

    nation, capital, population, rate = country


    nations.append(nation)
    capitals.append(capital)
    populations.append(population)
    rates.append(rate)

max_length_left = max(len(nation) for nation in nations) + max(len(capital) for capital in capitals)
max_length_right = max(len(str(population)) for population in populations) + max(len(str(rate)) for rate in rates)
print(max_length_left)
print(max_length_right)

for country in countries:
    print(f"{country[0]}.{country[1]:<{max_length_left-10}} = {str(country[2]) + ",":>{max_length_right - 10}} {country[3]:<.2f}")

file.close()






