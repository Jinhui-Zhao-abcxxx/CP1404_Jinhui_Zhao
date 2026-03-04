"""
Wimbledon
Estimate: 30 minutes

Actual: minutes
"""


def main():
    """a program to read this file, process the data and display processed information"""
    file = open("wimbledon.csv", "r", encoding="utf-8-sig")

    data = []
    champion_to_wins = {}
    time_to_champion_to_country = {}
    champions = []
    countries = []

    for line in file:
        data.append(line.split(","))

    data.pop(0)
    collect_data(data, time_to_champion_to_country)

    count_champion_wins(champion_to_wins, champions, time_to_champion_to_country)

    for champion, win in champion_to_wins.items():
        print(f"{champion} {win}")

    count_countries(countries, time_to_champion_to_country)

    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(f",".join(country for country in countries))

    file.close()


def count_countries(countries, time_to_champion_to_country):
    """count which and how many countries took part """
    for time in time_to_champion_to_country:
        if time_to_champion_to_country[time][1] not in countries:
            countries.append(time_to_champion_to_country[time][1])


def count_champion_wins(champion_to_wins, champions,
                        time_to_champion_to_country):
    """count how many champions and how many times they won"""
    for champion in time_to_champion_to_country.values():
        if champion[0] in champions:
            champion_to_wins[champion[0]] += 1
        else:
            champion_to_wins[champion[0]] = 1
            champions.append(champion[0])


def collect_data(data, time_to_champion_to_country):
    """getting useful data"""
    for info in data:
        time_to_champion_to_country[info[0]] = info[2], info[1]
    print(time_to_champion_to_country)


main()



