"""
CP1404/CP5632 Assignment 1 – Travel Tracker 1.0
Jinhui.Zhao
"""
import random
from operator import itemgetter

MENU = "Menu: \nD - Display all places \nR - Recommend a random place \nA - Add a new place \nM - Mark a place as visited \nQ - Quit "



def main():
    print("Travel Tracker 1.0 - by Jinhui.Zhao")

    original_places = read_csv()

    # print(original_places)
    # this is used for testing

    visited_places,unvisited_places = clean_data(original_places)

    # print(visited_places)
    # print(unvisited_places)
    # this is used for testing

    print(f"{len(original_places)} places loaded from places.csv")

    show_menu()

    user_input = input(">>>".lower())
    while user_input != "q":

        if user_input == "d":

            max_length_name = max(get_max_length(0,visited_places),get_max_length(0,unvisited_places))
            max_length_country = max(get_max_length(1,visited_places),get_max_length(1,unvisited_places))

            # print(max_length_name)
            # print(max_length_country)
            # this is used for testing

            display_number = 0

            display_places(display_number, max_length_country, max_length_name,unvisited_places,visited_places)

            user_input = input(">>>".lower())

        elif user_input == "r":

            if len(unvisited_places) == 0:
                print("No places left to visit!")

            else:
                random_number = random.randint(0,len(unvisited_places) - 1)
                print("Not sure where to visit next?")
                print(f"How about...  {unvisited_places[random_number][0]:>{len(unvisited_places[random_number][0])}} in {unvisited_places[random_number][1]:>{len(unvisited_places[random_number][1])}}?")

            user_input = input(">>>".lower())

        elif user_input == "a":
            new_place = []
            is_pass = False
            new_name = check_blank("Name:")
            new_country = check_blank("Country:")
            new_priority = check_if_valid(is_pass,"priority:")
            new_place.append(new_name)
            new_place.append(new_country)
            new_place.append(new_priority)

            # print(new_place)
            # this is used for testing

            user_input = input(">>>".lower())


def check_if_valid(is_pass,promo):

    while not is_pass:
        try:
            new_thing = int(input(promo))

            if new_thing <= 0:
                print("Number must be > 0")
            else:
                is_pass = True
        except ValueError:
            print("Invalid input; enter a valid number")

    return new_thing


def check_blank(promo):
    new_thing = input(promo)
    while new_thing == "":
        print("Input can not be blank")
        new_thing = input(promo)
    return new_thing


def display_places(display_number, max_length_country, max_length_name,unvisited_places,visited_places,):

    for place in unvisited_places:
        display_number += 1
        print(f"*{display_number}. {place[0]:<{max_length_name}} in {place[1]:<{max_length_country}} {place[2]}")

    for place in visited_places:
        display_number += 1
        print(f"{display_number}. {place[0]:<{max_length_name}} in {place[1]:<{max_length_country}} {place[2]}")



def clean_data(original_places):
    visited_places = []
    unvisited_places = []
    for place_info in original_places:
        if place_info[-2] == "n":
            unvisited_places.append(place_info[:-1].split(","))
        else:
            visited_places.append(place_info[:-1].split(","))

    unvisited_places.sort(key = itemgetter(2))
    unvisited_places.reverse()

    return visited_places,unvisited_places

def read_csv():
    places_file = open("places.csv", "r")
    original_places = places_file.readlines()
    places_file.close()
    return original_places


def show_menu():
    print(MENU)

def get_max_length(position,places_list):
    measuring_list = []
    for place in places_list:
        measuring_list.append(place[position])
    return len(max(measuring_list))





main()